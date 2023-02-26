import threading
import time

class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None
        self.playing = False
        self.pause = False
        self.lock = threading.Lock()

    def add_song(self, title, duration):
        song = Song(title, duration)
        node = PlaylistNode(song)

        with self.lock:
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next_node = node
                node.prev_node = self.tail
                self.tail = node

    def play(self):
        with self.lock:
            if not self.playing and not self.pause:
                self.playing = True
                self.current_node = self.head
                self._play_song(self.current_node.song)

    def pause(self):
        with self.lock:
            if self.playing and not self.pause:
                self.pause = True

    def resume(self):
        with self.lock:
            if self.playing and self.pause:
                self.pause = False
                self._play_song(self.current_node.song)

    def next(self):
        with self.lock:
            if self.current_node.next_node is not None:
                self._stop_song()
                self.current_node = self.current_node.next_node
                self._play_song(self.current_node.song)

    def prev(self):
        with self.lock:
            if self.current_node.prev_node is not None:
                self._stop_song()
                self.current_node = self.current_node.prev_node
                self._play_song(self.current_node.song)

    def _play_song(self, song):
        t = threading.Thread(target=self._play, args=(song,))
        t.start()

    def _play(self, song):
        time.sleep(song.duration)
        with self.lock:
            if not self.pause:
                self.next()

    def _stop_song(self):
        pass

class PlaylistNode:
    def __init__(self, song):
        self.song = song
        self.prev_node = None
        self.next_node = None