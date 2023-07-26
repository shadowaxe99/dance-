```python
from typing import List

class DanceStyle:
    def __init__(self, name: str, description: str, difficulty: str):
        self.name = name
        self.description = description
        self.difficulty = difficulty

class DanceStyleSchema:
    def __init__(self, dance_styles: List[DanceStyle]):
        self.dance_styles = dance_styles

def selectDanceStyle(userProfile, selectedDanceStyle):
    userProfile['selectedDanceStyle'] = selectedDanceStyle
    return userProfile

# List of available dance styles
dance_styles = [
    DanceStyle("Contemporary", "A style of expressive dance combining elements of several dance genres.", "Intermediate"),
    DanceStyle("Hip-Hop", "A dance style primarily performed to hip-hop music or that have evolved as part of hip-hop culture.", "Beginner"),
    DanceStyle("Ballet", "A type of performance dance that originated during the Italian Renaissance.", "Advanced"),
    DanceStyle("Salsa", "A lively, vigorous type of contemporary Latin American popular music.", "Intermediate"),
]

# Schema for dance styles
dance_style_schema = DanceStyleSchema(dance_styles)
```