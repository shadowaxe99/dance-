```python
import unittest
from src import user_interface

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = user_interface.UserInterface()

    def test_selectDanceStyle(self):
        self.ui.selectDanceStyle('hip-hop')
        self.assertEqual(self.ui.selectedDanceStyle, 'hip-hop')

    def test_selectMusicTrack(self):
        self.ui.selectMusicTrack('track1.mp3')
        self.assertEqual(self.ui.selectedMusicTrack, 'track1.mp3')

    def test_updateSubscription(self):
        self.ui.updateSubscription('premium')
        self.assertEqual(self.ui.subscriptionStatus, 'premium')

    def test_makeInAppPurchase(self):
        self.ui.makeInAppPurchase('extra_dance_styles')
        self.assertIn('extra_dance_styles', self.ui.inAppPurchases)

    def test_updatePartnershipStatus(self):
        self.ui.updatePartnershipStatus('partner1')
        self.assertEqual(self.ui.partnershipStatus, 'partner1')

if __name__ == '__main__':
    unittest.main()
```