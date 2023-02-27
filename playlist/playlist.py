import threading
import time

class Song:
    def __init__(self, title, duration):
        #Title of a song
        self.title = title
        # The duration of the song
        self.duration = duration

class Playlist:
    def __init__(self):
        self.songs = []
        self.current_song_index = -1
        self.playing = False
        self.pause = False
        self.next_song_event = threading.Event()

    def add_song(self, song):
        self.songs.append(song)

    def play(self):
        if self.playing:
            return
        if self.current_song_index == -1:
            self.current_song_index = 0
        song = self.songs[self.current_song_index]
        self.playing = True
        self.pause = False
        duration = min(song.duration, song.Duration)
        t = threading.Thread(target=self._play_song, args=(duration,))
        t.start()

    def _play_song(self, duration):
        time.sleep(duration)
        self.playing = False
        self.pause = False
        self.next_song_event.set()

    def pause(self):
        self.pause = True

    def resume(self):
        self.pause = False

    def next_song(self):
        if self.playing:
            self.pause = True
            self.next_song_event.set()
        self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.play()

    def prev_song(self):
        if self.playing:
            self.pause = True
            self.next_song_event.set()
        self.current_song_index = (self.current_song_index - 1) % len(self.songs)
        self.play()
