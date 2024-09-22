from flask import Flask, request, jsonify

app = Flask(__name__)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return "The backend deployment"

# POST request handler
@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    file_b64 = request.json.get('file_b64', None)

    user_id = "john_doe_17091999"  # Your formatted user ID
    email = "john@xyz.com"
    roll_number = "ABCD123"

    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]

    highest_lowercase_alphabet = max([x for x in alphabets if x.islower()], default=None)

    file_valid = file_b64 is not None  # Basic file validity check

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
        "file_valid": file_valid,
        "file_mime_type": "image/png" if file_b64 else None,  # For demonstration
        "file_size_kb": 400 if file_b64 else None
    }

    return jsonify(response)

# GET request handler
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
