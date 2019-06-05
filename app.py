#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

users = [
    {
        'id': 1,
        'name': u'Ajay Patel',
        'description': u'Spica developer',
        'role': u'developer'
    },
    {
        'id': 2,
        'name': u'Ajay',
        'description': u'Observer access',
        'role': u'Observer'
    }
]

@app.route('/vault/v1.0/users', methods=['GET'])
def get_users():
    return jsonify({'user': users})

@app.route('/vault/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/vault/v1.0/users', methods=['POST'])
def create_user():
    user = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', ""),
        'role': request.json.get('role')
    }
    users.append(user)
    return jsonify({'user': user}), 201

@app.route('/vault/v1.0/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'role' in request.json and type(request.json['done']) is not unicode:
        abort(400)
    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['description'] = request.json.get('description', user[0]['description'])
    user[0]['role'] = request.json.get('role', user[0]['role'])
    return jsonify({'user': user[0]})

@app.route('/vault/v1.0/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
