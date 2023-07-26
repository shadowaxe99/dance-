```python
import unittest
from src import partnerships

class TestPartnerships(unittest.TestCase):

    def setUp(self):
        self.partnership = partnerships.Partnership()

    def test_update_partnership_status(self):
        # Test updating partnership status
        self.partnership.updatePartnershipStatus("active")
        self.assertEqual(self.partnership.partnershipStatus, "active")

        # Test invalid status
        with self.assertRaises(ValueError):
            self.partnership.updatePartnershipStatus("invalid")

    def test_get_partnership_status(self):
        # Test getting partnership status
        self.partnership.updatePartnershipStatus("active")
        status = self.partnership.getPartnershipStatus()
        self.assertEqual(status, "active")

    def test_get_partnership_details(self):
        # Test getting partnership details
        self.partnership.updatePartnershipStatus("active")
        details = self.partnership.getPartnershipDetails()
        self.assertEqual(details, {"status": "active"})

if __name__ == '__main__':
    unittest.main()
```