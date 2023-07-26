```python
import unittest
from src import motion_analysis

class TestMotionAnalysis(unittest.TestCase):

    def setUp(self):
        self.motionData = {
            "user_id": 1,
            "dance_moves": [
                {"move_name": "twist", "duration": 2, "technique_score": 8},
                {"move_name": "jump", "duration": 1, "technique_score": 7}
            ]
        }

    def test_analyzeMotionData(self):
        result = motion_analysis.analyzeMotionData(self.motionData)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('analysis_result', result)

    def test_invalidMotionData(self):
        with self.assertRaises(ValueError):
            motion_analysis.analyzeMotionData(None)

        with self.assertRaises(ValueError):
            motion_analysis.analyzeMotionData({})

        with self.assertRaises(ValueError):
            motion_analysis.analyzeMotionData({"user_id": 1})

    def test_analysisResult(self):
        result = motion_analysis.analyzeMotionData(self.motionData)
        self.assertIn('total_moves', result['analysis_result'])
        self.assertIn('total_duration', result['analysis_result'])
        self.assertIn('average_technique_score', result['analysis_result'])

if __name__ == '__main__':
    unittest.main()
```