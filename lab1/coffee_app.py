from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user database
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Here you would typically add the user to your database
    # For simplicity, we'll just store them in memory
    users[email] = {'password': password}

    # Send a welcome message
    welcome_message = f"Welcome to our coffee shop app, {email}!"
    
    return jsonify({'message': welcome_message})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Check if the user exists and the password matches
    if email in users and users[email]['password'] == password:
        # Assuming successful login
        return jsonify({'message': 'Login successful!'})

    return jsonify({'message': 'Invalid email or password'})

@app.route('/google_login', methods=['POST'])
def google_login():
    data = request.json
    email = data.get('email')

    # Check if the user is registering for the first time with Google
    if email not in users:
        # Here you would typically add the user to your database
        # For simplicity, we'll just store them in memory
        users[email] = {'password': None}

        # Send a welcome message
        welcome_message = f"Welcome to our coffee shop app, {email}!"
    
        return jsonify({'message': welcome_message})

    return jsonify({'message': 'Welcome back!'})

if __name__ == '__main__':
    app.run(debug=True)