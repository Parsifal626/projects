from threading import Thread, Lock
import time

#The Playlist class implements all the functionality for managing a playlist,
# using a doubly linked list to store a list of songs.
class Playlist:
    def __init__(self):
        self.__songs = []
        self.__current_song_index = 0
        self.__play_thread = None
        self.__play_thread_lock = Lock()
        self.__is_playing = False

#The play method starts playing the current song.
#If the song is already playing, nothing happens.
    def play(self):
        if self.__play_thread is None or not self.__play_thread.is_alive():
            self.__play_thread_lock.acquire()
            self.__is_playing = True
            self.__play_thread = Thread(target=self.__play_current_song)
            self.__play_thread.start()
            self.__play_thread_lock.release()

# do nothing if there is no current song
    def pause(self):
        if self.__play_thread is not None and self.__is_playing:
            self.__play_thread_lock.acquire()
            self.__is_playing = False
            self.__play_thread_lock.release()

    def add_song(self, song):
        self.__songs.append(song)

    def next_song(self):
        if self.__play_thread is not None:
            self.__play_thread_lock.acquire()
            self.__is_playing = False
            self.__play_thread.join()
            self.__play_thread_lock.release()

        self.__current_song_index +=1
        if self.__current_song_index >= len(self.__songs):
            self.__current_song_index = 0

        self.play()

    def prev_song(self):
        if self.__play_thread is not None:
            self.__play_thread_lock.acquire()
            self.__is_playing = False
            self.__play_thread.join()
            self.__play_thread_lock.release()

        self.__current_song_index -= 1
        if self.__current_song_index < 0:
            self.__current_song_index = len(self.__songs) - 1

        self.play()

    def __play_current_song(self):
        song = self.__songs[self.__current_song_index]
        duration = song.duration
        start_time = time.time()

        while self.__is_playing and time.time() - start_time < duration:
            time.sleep(0.1)

        self.__is_playing = False
        self.next_song()


import threading
import time

class Song:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Playlist:
    def __init__(self):
        self.current_song = None
        self.head = None
        self.tail = None
        self.lock = threading.Lock()

    def add_song(self, song):
        with self.lock:
            new_song = Song(song.name, song.duration)
            if self.tail is None:
                self.head = new_song
                self.tail = new_song
            else:
                new_song.prev = self.tail
                self.tail.next = new_song
                self.tail = new_song

    def play(self):
        if self.current_song is None:
            self.current_song = self.head
        while self.current_song is not None:
            print("Playing song:", self.current_song.name)
            duration = self.current_song.duration
            time.sleep(duration)
            self.current_song = self.current_song.next

    def pause(self):

        if self.current_song is None:
            return
        print("Pausing song:", self.current_song.name)
        self.current_song = self.current_song
        # TODO: implement resume functionality

    def next_song(self):
        # do nothing if there is no current song
        if self.current_song is None:
            return
        print("Stopping song:", self.current_song.name)
        self.current_song = self.current_song.next

    def prev_song(self):
        # do nothing if there is no current song
        if self.current_song is None:
            return
        print("Stopping song:", self.current_song.name)
        self.current_song = self.current_song.prev
