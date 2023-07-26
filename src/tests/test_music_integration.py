```python
import unittest
from src import music_integration

class TestMusicIntegration(unittest.TestCase):

    def setUp(self):
        self.music_integration = music_integration.MusicIntegration()
        self.userProfile = {
            "username": "test_user",
            "selectedDanceStyle": "hip-hop",
            "selectedMusicTrack": None
        }
        self.musicTrack = {
            "title": "Test Track",
            "artist": "Test Artist",
            "genre": "Hip-Hop",
            "duration": 180
        }

    def test_selectMusicTrack(self):
        self.music_integration.selectMusicTrack(self.userProfile, self.musicTrack)
        self.assertEqual(self.userProfile["selectedMusicTrack"], self.musicTrack)

    def test_musicTrackSelection(self):
        self.music_integration.musicTrackSelection(self.userProfile, self.musicTrack)
        self.assertEqual(self.userProfile["selectedMusicTrack"], self.musicTrack)

    def test_musicTrackMatchesDanceStyle(self):
        is_match = self.music_integration.musicTrackMatchesDanceStyle(self.userProfile, self.musicTrack)
        self.assertTrue(is_match)

if __name__ == '__main__':
    unittest.main()
```