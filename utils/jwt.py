import jwt
from utils.config import Config


def encode_token(payload):
    return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')


def decode_token(token):
    return jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
