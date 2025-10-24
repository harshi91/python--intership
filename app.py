from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = []

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user by id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        user.update({
            "name": data.get("name", user["name"]),
            "email": data.get("email", user["email"])
        })
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    if any(u['id'] == user_id for u in users):
        users = [u for u in users if u['id'] != user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
