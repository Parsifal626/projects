client = PlaylistClient('localhost:50051')

# get the playlist
playlist = client.get_playlist()

# add a song to the playlist
song = {'title': 'Song Title', 'artist': 'Artist Name', 'duration': 180}
client.add_song(song)

# remove a song from the playlist
client.remove_song(song)

# play the playlist
client.play()

# pause the current song
client.pause()

# stop playing the playlist
client.stop()

# skip to the next song
client.next()

# skip to the previous song
client.previous()
