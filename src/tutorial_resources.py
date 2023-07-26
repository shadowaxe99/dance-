```python
from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['ai_dance_choreographer']
tutorial_resources_collection = db['tutorial_resources']

# Schema for tutorial resources
TutorialResourceSchema = {
    'title': str,
    'description': str,
    'video_url': str,
    'dance_style': str,
    'difficulty_level': str
}

def accessTutorialResource(userProfile, resource_id):
    """
    Function to access a specific tutorial resource
    """
    resource = tutorial_resources_collection.find_one({'_id': ObjectId(resource_id)})
    if resource:
        print(f"Accessing tutorial resource: {resource['title']}")
        tutorialResources[userProfile] = resource
        return resource
    else:
        print("Tutorial resource not found.")
        return None

def addTutorialResource(resource):
    """
    Function to add a new tutorial resource
    """
    if isinstance(resource, dict) and all(key in TutorialResourceSchema for key in resource.keys()):
        tutorial_resources_collection.insert_one(resource)
        print(f"Added tutorial resource: {resource['title']}")
    else:
        print("Invalid resource format.")

def updateTutorialResource(resource_id, updated_resource):
    """
    Function to update an existing tutorial resource
    """
    if isinstance(updated_resource, dict) and all(key in TutorialResourceSchema for key in updated_resource.keys()):
        tutorial_resources_collection.update_one({'_id': ObjectId(resource_id)}, {"$set": updated_resource})
        print(f"Updated tutorial resource: {updated_resource['title']}")
    else:
        print("Invalid resource format.")

def deleteTutorialResource(resource_id):
    """
    Function to delete a tutorial resource
    """
    tutorial_resources_collection.delete_one({'_id': ObjectId(resource_id)})
    print(f"Deleted tutorial resource with id: {resource_id}")
```