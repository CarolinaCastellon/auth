from flask import Flask, request, jsonify
from controllers import auth
from flask_cors import CORS, cross_origin
from utils.config import Config

app = Flask(__name__)

CORS(app)


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    body = request.get_json()

    if 'email' not in body or 'password' not in body:
        return jsonify({'error': 'No data in body'}), 400

    user, code_status = auth.login(
        email=body['email'], password=body['password'])

    return jsonify(user), code_status


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    body = request.get_json()

    if 'name' not in body or 'email' not in body or 'password' not in body:
        return jsonify({'error': 'No data in body'}), 400

    auth.register(name=body['name'], email=body['email'],
                  password=body['password'])

    return {'message': 'You are now registered!', 'success': True}, 200


if __name__ == '__main__':
    app.run(port=Config.PORT)
