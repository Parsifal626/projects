from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/songs.db', methods=['GET'])
def get_songs():
    songs = ['Song 1', 'Song 2']
    # код для получения списка песен из конфигурационного файла
    # возвращает список песен в формате JSON
    return jsonify(songs)

@app.route('/api/songs', methods=['POST'])
def add_song():
    # код для добавления песни в конфигурационный файл
    # возвращает статус 201 (Created) в случае успеха
    return '', 201

@app.route('/api/songs/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    # код для обновления песни в конфигурационном файле
    # возвращает статус 204 (No Content) в случае успеха
    return '', 204

@app.route('/api/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    # код для удаления песни из конфигурационного файла
    # возвращает статус 204 (No Content) в случае успеха
    return '', 204

@app.route('/api/play', methods=['POST'])
def play_song():
    # код для воспроизведения песни
    # возвращает статус 200 (OK) в случае успеха
    return '', 200

@app.route('/api/pause', methods=['POST'])
def pause_song():
    # код для приостановки воспроизведения песни
    # возвращает статус 200 (OK) в случае успеха
    return '', 200

@app.route('/api/next', methods=['POST'])
def next_song():
    # код для перехода к следующей песне
    # возвращает статус 200 (OK) в случае успеха
    return '', 200