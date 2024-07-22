from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    chunks = db.relationship('FileChunk', backref='file', lazy=True)

    def __repr__(self):
        return (f"<File(id={self.id}, filename='{self.filename}', created_at='{self.created_at}', "
                f"updated_at='{self.updated_at}')>")


class FileChunk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)
    chunk_data = db.Column(db.LargeBinary, nullable=False)
    chunk_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<FileChunk(id={self.id}, file_id={self.file_id}, chunk_number={self.chunk_number})>"

    __table_args__ = (
        db.UniqueConstraint('file_id', 'chunk_number', name='_file_chunk_uc'),
    )
