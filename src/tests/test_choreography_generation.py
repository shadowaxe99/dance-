```python
import unittest
from src import choreography_generation

class TestChoreographyGeneration(unittest.TestCase):

    def setUp(self):
        self.userProfile = {
            "name": "Test User",
            "selectedDanceStyle": "Hip-Hop",
            "selectedMusicTrack": "test_track.mp3",
            "motionData": {},
            "subscriptionStatus": "Free"
        }
        self.motionData = {
            "move1": {"x": 10, "y": 20, "z": 30},
            "move2": {"x": 40, "y": 50, "z": 60}
        }

    def test_generateChoreography(self):
        choreography = choreography_generation.generateChoreography(self.userProfile, self.motionData)
        self.assertIsNotNone(choreography)
        self.assertIsInstance(choreography, dict)
        self.assertIn('choreographySteps', choreography)

    def test_generateChoreography_noMotionData(self):
        with self.assertRaises(ValueError):
            choreography_generation.generateChoreography(self.userProfile, {})

    def test_generateChoreography_noDanceStyle(self):
        self.userProfile["selectedDanceStyle"] = None
        with self.assertRaises(ValueError):
            choreography_generation.generateChoreography(self.userProfile, self.motionData)

    def test_generateChoreography_noMusicTrack(self):
        self.userProfile["selectedMusicTrack"] = None
        with self.assertRaises(ValueError):
            choreography_generation.generateChoreography(self.userProfile, self.motionData)

if __name__ == '__main__':
    unittest.main()
```