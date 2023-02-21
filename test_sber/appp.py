from flask import Flask, jsonify, request

# Создание Flask-приложения
app = Flask(__name__)

# Настройка подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация экземпляра SQLAlchemy и Marshmallow
db.init_app(app)
ma.init_app(app)

# Создание таблиц в базе данных
with app.app_context():
    db.create_all()

# Методы для выполнения CRUD операций с песнями в плейлисте

# Получение списка всех песен в плейлисте
@app.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    song_schema = SongSchema(many=True)
    result = song_schema.dump(songs)
    return jsonify(result)

# Получение конкретной песни из плейлиста
@app.route('/songs/<int:id>', methods=['GET'])
def get_song(id):
    song = Song.query.get(id)
    if song:
        song_schema = SongSchema()
        result = song_schema.dump(song)
        return jsonify(result)
    else:
        return jsonify({'error': 'Song not found'}), 404

# Добавление новой песни в плейлист
@app.route('/songs', methods=['POST'])
def add_song():
    title = request.json['title']
    artist = request.json['artist']
    duration = request.json['duration']
    song = Song(title=title, artist=artist, duration=duration)
    db.session.add(song)
    db.session.commit()
    song_schema = SongSchema()
    result = song_schema.dump(song)
    return jsonify(result)

# Обновление существующей песни в плейлисте
@app.route('/songs/<int:id>', methods=['PUT'])
def update_song(id):
    song = Song.query.get(id)
    if song:
        title = request.json['title']
        artist = request.json['artist']
        duration = request.json['duration']
        song.title = title
        song.artist = artist
        song.duration
