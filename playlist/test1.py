import unittest
from playlist import Playlist, Song

class TestPlaylist(unittest.TestCase):

    def test_add_song(self):
        playlist = Playlist()
        song = Song("Test song", 120)
        playlist.add_song(song)
        self.assertEqual(len(playlist), 1)

    def test_play_pause(self):
        playlist = Playlist()
        song1 = Song("Song 1", 120)
        song2 = Song("Song 2", 180)
        playlist.add_song(song1)
        playlist.add_song(song2)
        playlist.play()
        self.assertTrue(playlist.is_playing())
        playlist.pause()
        self.assertFalse(playlist.is_playing())

    def test_next_prev(self):
        playlist = Playlist()
        song1 = Song("Song 1", 120)
        song2 = Song("Song 2", 180)
        song3 = Song("Song 3", 200)
        playlist.add_song(song1)
        playlist.add_song(song2)
        playlist.add_song(song3)
        playlist.play()
        self.assertEqual(playlist.current_song(), song1)
        playlist.next()
        self.assertEqual(playlist.current_song(), song2)
        playlist.next()
        self.assertEqual(playlist.current_song(), song3)
        playlist.prev()
        self.assertEqual(playlist.current_song(), song2)

if __name__ == '__main__':
    unittest.main()
