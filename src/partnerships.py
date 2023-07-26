```python
from pymongo import MongoClient
from bson.objectid import ObjectId

class Partnership:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['dance_app']
        self.collection = self.db['partnerships']

    def create_partnership(self, partnership_data):
        result = self.collection.insert_one(partnership_data)
        return str(result.inserted_id)

    def get_partnership(self, partnership_id):
        result = self.collection.find_one({'_id': ObjectId(partnership_id)})
        return result

    def update_partnership(self, partnership_id, partnership_data):
        self.collection.update_one({'_id': ObjectId(partnership_id)}, {"$set": partnership_data})
        return self.get_partnership(partnership_id)

    def delete_partnership(self, partnership_id):
        self.collection.delete_one({'_id': ObjectId(partnership_id)})
        return True

def updatePartnershipStatus(user_id, partnership_id, status):
    partnership = Partnership()
    partnership_data = partnership.get_partnership(partnership_id)
    if partnership_data:
        partnership_data['status'] = status
        partnership.update_partnership(partnership_id, partnership_data)
        return True
    return False
```