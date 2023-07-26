```python
import datetime
from collections import defaultdict

class Metrics:
    def __init__(self):
        self.user_engagement = defaultdict(int)
        self.customer_retention = defaultdict(int)
        self.user_feedback = defaultdict(list)

    def track_user_engagement(self, user_id, action):
        self.user_engagement[user_id] += 1
        self.user_engagement[action] += 1

    def track_customer_retention(self, user_id, subscription_status):
        if subscription_status:
            self.customer_retention[user_id] += 1

    def track_user_feedback(self, user_id, rating, review):
        self.user_feedback[user_id].append((rating, review, datetime.datetime.now()))

    def get_user_engagement(self, user_id=None, action=None):
        if user_id:
            return self.user_engagement[user_id]
        elif action:
            return self.user_engagement[action]
        else:
            return self.user_engagement

    def get_customer_retention(self, user_id=None):
        if user_id:
            return self.customer_retention[user_id]
        else:
            return self.customer_retention

    def get_user_feedback(self, user_id=None):
        if user_id:
            return self.user_feedback[user_id]
        else:
            return self.user_feedback
```