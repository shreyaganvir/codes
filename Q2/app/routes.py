import os

from flask_restful import Resource, reqparse
from flask import send_file
from werkzeug.datastructures import FileStorage
from .models import db, File, FileChunk
from .config import Config
import io


class FileResource(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files', required=True)
        args = parser.parse_args()
        file_storage = args['file']
        filename = file_storage.filename

        file_record = File.query.filter_by(filename=filename).first()
        if not file_record:
            file_record = File(filename=filename)
            db.session.add(file_record)
            db.session.commit()
            message = f"New file created: {file_record}"
        else:
            message = f"File record found: {file_record}"

        chunk_number = FileChunk.query.filter_by(file_id=file_record.id).count() + 1
        file_chunk = FileChunk(file_id=file_record.id, chunk_data=file_storage.read(), chunk_number=chunk_number)
        db.session.add(file_chunk)
        db.session.commit()

        return {
            'message': message,
            'file': repr(file_record),
            'file_chunk': repr(file_chunk)
        }, 201

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
