```python
import unittest
from src import dance_styles

class TestDanceStyles(unittest.TestCase):

    def setUp(self):
        self.dance_styles = dance_styles.DanceStyles()

    def test_select_dance_style(self):
        self.dance_styles.selectDanceStyle('hip-hop')
        self.assertEqual(self.dance_styles.selectedDanceStyle, 'hip-hop')

    def test_invalid_dance_style(self):
        with self.assertRaises(ValueError):
            self.dance_styles.selectDanceStyle('invalid-style')

    def test_get_dance_styles(self):
        dance_styles = self.dance_styles.getDanceStyles()
        self.assertIn('contemporary', dance_styles)
        self.assertIn('hip-hop', dance_styles)
        self.assertIn('ballet', dance_styles)
        self.assertIn('salsa', dance_styles)

if __name__ == '__main__':
    unittest.main()
```