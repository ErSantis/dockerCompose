from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route('/signup', methods=['POST'])
def sign_up():
    data = request.json
    username = data['username']
    password = data['password']
    if username in users:
        return jsonify({"message": "User already exists"}), 400
    users[username] = password
    return jsonify({"message": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def log_in():
    data = request.json
    username = data['username']
    password = data['password']
    if username not in users or users[username] != password:
        return jsonify({"message": "Invalid credentials"}), 401
    return jsonify({"message": "Logged in successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
