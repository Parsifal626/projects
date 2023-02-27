from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from playlist import Playlist, Song

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
db = SQLAlchemy(app)

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Track(id={self.id}, title={self.title}, artist={self.artist}, duration={self.duration})'

@app.route('/tracks', methods=['GET'])
def get_all_tracks():
    tracks = Track.query.all()
    return jsonify([track.__dict__ for track in tracks]), 200

@app.route('/tracks/<int:track_id>', methods=['GET'])
def get_track(track_id):
    track = Track.query.filter_by(id=track_id).first()
    if track:
        return jsonify(track.__dict__), 200
    else:
        return jsonify({'message': 'Track not found'}), 404

@app.route('/tracks', methods=['POST'])
def create_track():
    data = request.get_json()
    track = Track(title=data['title'], artist=data['artist'], duration=data['duration'])
    db.session.add(track)
    db.session.commit()
    return jsonify(track.__dict__), 201

@app.route('/tracks/int:track_id', methods=['PUT'])
def update_track(track_id):
    track = Track.query.filter_by(id=track_id).first()
    if track:
        data = request.get_json()
        track.title = data.get('title', track.title)
        track.artist = data.get('artist', track.artist)
        track.duration = data.get('duration', track.duration)
        db.session.commit()
        return jsonify(track.dict), 200
    else:
        return jsonify({'message': 'Track not found'}), 404@app.route('/tracks/int:track_id', methods=['DELETE'])
def delete_track(track_id):
    track = Track.query.filter_by(id=track_id).first()
    if track:
        db.session.delete(track)
        db.session.commit()
        return jsonify({'message': 'Track deleted successfully'}), 200
    else:
        return jsonify({'message': 'Track not found'})
