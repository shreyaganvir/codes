import os

from flask_restful import Resource, reqparse
from flask import send_file, request
from .models import db, File, FileChunk
from .config import Config
import io


class FileResource(Resource):

    @staticmethod
    def post():
        if 'file' not in request.files:
            return {'message': 'No file part in the request'}, 400

        files = request.files.getlist('file')
        if not files:
            return {'message': 'No file provided'}, 400

        responses = []
        for file_storage in files:
            filename = file_storage.filename

            # Check if the file already exists
            file_record = File.query.filter_by(filename=filename).first()
            if not file_record:
                file_record = File(filename=filename)
                db.session.add(file_record)
                db.session.commit()
                message = f"New file created: {file_record}"
            else:
                message = f"File record found: {file_record}"

            # Add the file chunk
            chunk_number = FileChunk.query.filter_by(file_id=file_record.id).count() + 1
            file_chunk = FileChunk(file_id=file_record.id, chunk_data=file_storage.read(), chunk_number=chunk_number)
            db.session.add(file_chunk)
            db.session.commit()

            # Collect response for this file
            response = {
                'message': message,
                'file': repr(file_record),
                'file_chunk': repr(file_chunk)
            }
            responses.append(response)

        return responses, 201

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('filename', required=True, type=str)
        args = parser.parse_args()

        file_record = File.query.filter_by(filename=args['filename']).first()
        if not file_record:
            return {'message': 'File not found'}, 404

        chunks = FileChunk.query.filter_by(file_id=file_record.id).order_by(FileChunk.chunk_number).all()
        file_data = b''.join(chunk.chunk_data for chunk in chunks)
        filedata = io.BytesIO(file_data)
        filename = args['filename']

        # Save to a temporary file
        if not (os.path.exists(Config.OUT_DIR)):
            os.mkdir(Config.OUT_DIR)
        temp_file_path = os.path.join(Config.OUT_DIR, filename)
        with open(temp_file_path, 'wb') as f:
            f.write(filedata.getvalue())

        return send_file(
            filedata,
            mimetype='application/octet-stream'
        )
