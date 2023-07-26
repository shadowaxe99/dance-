```python
import unittest
from src import monetization

class TestMonetization(unittest.TestCase):

    def setUp(self):
        self.userProfile = {
            "username": "test_user",
            "subscriptionStatus": "free",
            "inAppPurchases": []
        }
        self.subscriptionSchema = {
            "type": "premium",
            "price": 9.99
        }
        self.inAppPurchaseSchema = {
            "type": "additional_dance_style",
            "price": 1.99
        }

    def test_updateSubscription(self):
        monetization.updateSubscription(self.userProfile, self.subscriptionSchema)
        self.assertEqual(self.userProfile["subscriptionStatus"], "premium")

    def test_makeInAppPurchase(self):
        monetization.makeInAppPurchase(self.userProfile, self.inAppPurchaseSchema)
        self.assertIn(self.inAppPurchaseSchema, self.userProfile["inAppPurchases"])

if __name__ == '__main__':
    unittest.main()
```