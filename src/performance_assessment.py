```python
from src.user_interface import userProfile
from src.motion_analysis import motionData
from src.choreography_generation import generatedChoreography
from src.customization import customizedChoreography

class FeedbackSchema:
    def __init__(self, user_id, feedback, score):
        self.user_id = user_id
        self.feedback = feedback
        self.score = score

performanceFeedback = []

def assessPerformance(user_id, feedback, score):
    """
    Function to assess user's performance and provide feedback
    """
    new_feedback = FeedbackSchema(user_id, feedback, score)
    performanceFeedback.append(new_feedback)
    return new_feedback

def getPerformanceFeedback(user_id):
    """
    Function to get user's performance feedback
    """
    user_feedback = [feedback for feedback in performanceFeedback if feedback.user_id == user_id]
    return user_feedback

def updatePerformanceFeedback(user_id, feedback, score):
    """
    Function to update user's performance feedback
    """
    for fb in performanceFeedback:
        if fb.user_id == user_id:
            fb.feedback = feedback
            fb.score = score
    return getPerformanceFeedback(user_id)
```