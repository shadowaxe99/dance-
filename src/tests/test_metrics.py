```python
import unittest
from src import metrics

class TestMetrics(unittest.TestCase):

    def setUp(self):
        self.userProfile = {
            'username': 'testUser',
            'email': 'testUser@example.com',
            'subscriptionStatus': 'free',
            'inAppPurchases': []
        }
        self.metrics = metrics.Metrics(self.userProfile)

    def test_user_engagement(self):
        self.metrics.update_engagement('timeSpent', 120)
        self.metrics.update_engagement('routinesCreated', 5)
        self.metrics.update_engagement('interactions', 10)
        engagement = self.metrics.get_engagement()
        self.assertEqual(engagement['timeSpent'], 120)
        self.assertEqual(engagement['routinesCreated'], 5)
        self.assertEqual(engagement['interactions'], 10)

    def test_customer_retention(self):
        self.metrics.update_retention('activeDays', 30)
        self.metrics.update_retention('subscriptionStatus', 'premium')
        retention = self.metrics.get_retention()
        self.assertEqual(retention['activeDays'], 30)
        self.assertEqual(retention['subscriptionStatus'], 'premium')

    def test_user_feedback(self):
        self.metrics.update_feedback('usabilityRating', 4.5)
        self.metrics.update_feedback('routineQualityRating', 4.0)
        self.metrics.update_feedback('learningResourcesRating', 4.7)
        feedback = self.metrics.get_feedback()
        self.assertEqual(feedback['usabilityRating'], 4.5)
        self.assertEqual(feedback['routineQualityRating'], 4.0)
        self.assertEqual(feedback['learningResourcesRating'], 4.7)

if __name__ == '__main__':
    unittest.main()
```