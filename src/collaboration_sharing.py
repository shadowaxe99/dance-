```python
import json
from flask import Flask, request, jsonify
from src.user_interface import userProfile
from src.customization import customizedChoreography

app = Flask(__name__)

sharedChoreographies = []

@app.route('/share_choreography', methods=['POST'])
def share_choreography():
    data = request.get_json()
    choreography = data.get('choreography')
    user = data.get('user')
    if choreography and user:
        sharedChoreographies.append({
            'user': user,
            'choreography': choreography
        })
        return jsonify({'message': 'Choreography shared successfully!'}), 200
    else:
        return jsonify({'message': 'Invalid request. Please provide choreography and user.'}), 400

@app.route('/get_shared_choreographies', methods=['GET'])
def get_shared_choreographies():
    return jsonify({'sharedChoreographies': sharedChoreographies}), 200

@app.route('/collaborate', methods=['POST'])
def collaborate():
    data = request.get_json()
    collaborator = data.get('collaborator')
    choreography = data.get('choreography')
    if collaborator and choreography:
        for shared in sharedChoreographies:
            if shared['choreography'] == choreography:
                shared['collaborators'].append(collaborator)
                return jsonify({'message': 'Collaboration request sent!'}), 200
    return jsonify({'message': 'Invalid request. Please provide valid collaborator and choreography.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```