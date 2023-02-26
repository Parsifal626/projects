import timeit

# Создаем плейлист с 1000 песен
playlist = Playlist()
for i in range(1000):
    playlist.add_song(Song(f"Song{i}", 180))

# Запускаем воспроизведение и замеряем время
elapsed_time = timeit.timeit(playlist.play, number=1)
print(f"Elapsed time: {elapsed_time}")
