class Playlist:
    def __init__(self):
        self.songs = []  # список песен
        self.current_song = 0  # индекс текущей песни
        self.is_playing = False  # флаг воспроизведения

    def play(self):
        if not self.songs:
            print("Список песен пуст")
            return
        self.is_playing = True
        print(f"Воспроизводится песня '{self.songs[self.current_song]}'")

    def pause(self):
        if not self.songs:
            print("Список песен пуст")
            return
        self.is_playing = False
        print("Воспроизведение приостановлено")

    def add_song(self, song):
        self.songs.append(song)
        print(f"Песня '{song}' добавлена в плейлист")

    def next_song(self):
        if not self.songs:
            print("Список песен пуст")
            return
        self.current_song = (self.current_song + 1) % len(self.songs)
        if self.is_playing:
            print(f"Воспроизводится следующая песня '{self.songs[self.current_song]}'")

    def prev_song(self):
        if not self.songs:
            print("Список песен пуст")
            return
        self.current_song = (self.current_song - 1) % len(self.songs)
        if self.is_playing:
            print(f"Воспроизводится предыдущая песня '{self.songs[self.current_song]}'")


playlist = Playlist()
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Stairway to Heaven")
playlist.play()  # Воспроизводится песня 'Bohemian Rhapsody'
playlist.next_song()  # Воспроизводится следующая песня 'Stairway to Heaven'
playlist.prev_song()  # Воспроизводится предыдущая песня 'Bohemian Rhapsody'
playlist.pause()  # Воспроизведение приостановлено
