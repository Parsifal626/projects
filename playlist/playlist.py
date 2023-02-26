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


# add song in the end
    def add_song(self, song):
        self.__songs.append(song)

# play next song
    def next_song(self):
        if self.__play_thread is not None:
            self.__play_thread_lock.acquire()
            self.__is_playing = False
            self.__play_thread.join()
            self.__play_thread_lock.release()


        self.__current_song_index +=1
#if we reach the limit of songs we start from scratch
        if self.__current_song_index >= len(self.__songs):
            self.__current_song_index = 0

        self.play()

# play previous song
    def prev_song(self):
        if self.__play_thread is not None:
            self.__play_thread_lock.acquire()
            self.__is_playing = False
            self.__play_thread.join()
            self.__play_thread_lock.release()

        self.__current_song_index -= 1
# if we reach the first song we skip on the last song
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