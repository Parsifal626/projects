pip install flask
pip install sqlite3


from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DATABASE = 'playlist.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/api/songs', methods=['GET'])
def get_songs():
    db = get_db()
    cur = db.execute('SELECT * FROM songs')
    songs = cur.fetchall()
    return jsonify(songs)

@app.route('/api/songs/<int:id>', methods=['GET'])
def get_song(id):
    db = get_db()
    cur = db.execute('SELECT * FROM songs WHERE id = ?', (id,))
    song = cur.fetchone()
    return jsonify(song)

@app.route('/api/songs', methods=['POST'])
def add_song():
    title = request.json['title']
    artist = request.json['artist']
    duration = request.json['duration']

    db = get_db()
    db.execute('INSERT INTO songs (title, artist, duration) VALUES (?, ?, ?)',
               [title, artist, duration])
    db.commit()

    return jsonify({'result': True})

@app.route('/api/songs/<int:id>', methods=['PUT'])
def update_song(id):
    title = request.json['title']
    artist = request.json['artist']
    duration = request.json['duration']

    db = get_db()
    db.execute('UPDATE songs SET title = ?, artist = ?, duration = ? WHERE id = ?',
               [title, artist, duration, id])
    db.commit()

    return jsonify({'result': True})

@app.route('/api/songs/<int:id>', methods=['DELETE'])
def delete_song(id):
    db = get_db()
    db.execute('DELETE FROM songs WHERE id = ?', [id])
    db.commit()

    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)


    def get_all_songs(self) -> List[Song]:
    """Возвращает все песни в плейлисте"""
    return self._playlist.get_all_songs()

def add_song(self, song_data: dict) -> Song:
    """Добавляет новую песню в плейлист"""
    song = Song(**song_data)
    self._playlist.add_song(song)
    return song

