from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Создание экземпляров для работы с базой данных и сериализации/десериализации
db = SQLAlchemy()
ma = Marshmallow()

# Определение класса Song для представления песен
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

# Определение схемы для сериализации и десериализации объектов Song в JSON
class SongSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Song
        load_instance = True
