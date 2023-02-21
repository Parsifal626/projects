import grpc

import music_pb2
import music_pb2_grpc


class MusicClient:
    def __init__(self, host: str, port: int):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = music_pb2_grpc.MusicServiceStub(self.channel)

    def create_song(self, title: str, artist: str, duration: int) -> str:
        song = music_pb2.Song(title=title, artist=artist, duration=duration)
        response = self.stub.CreateSong(song)
        return response.song_id

    def get_song(self, song_id: str) -> music_pb2.Song:
        request = music_pb2.GetSongRequest(song_id=song_id)
        response = self.stub.GetSong(request)
        return response.song

    def update_song(self, song_id: str, title: str, artist: str, duration: int) -> None:
        song = music_pb2.Song(song_id=song_id, title=title, artist=artist, duration=duration)
        self.stub.UpdateSong(song)

    def delete_song(self, song_id: str) -> None:
        request = music_pb2.DeleteSongRequest(song_id=song_id)
        self.stub.DeleteSong(request
