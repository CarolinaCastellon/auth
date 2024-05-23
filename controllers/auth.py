from models.user import User
from utils.jwt import encode_token
from utils.bcrypt import hash_password, verify_password


def login(email, password):
    try:
        user = User.read_by_email(email)

        if not verify_password(bytes(password, 'utf-8'), bytes(user.password, 'utf-8')):
            return {
                'success': False,
                'message': 'Wrong password or email'
            }, 404

        res = {
            'success': True,
            'data': {
                'token': encode_token({'user_id': user.user_id}),
                'name': user.name,
                'email': user.email,
                'id': user.user_id
            }
        }

        return res, 200

    except Exception as e:
        return {'success': False, 'message': 'Something was wrong'}, 500


def register(name, email, password):
    bytes_pass = bytes(password, 'utf-8')

    hashed = str(hash_password(bytes_pass).decode('utf-8'))
    user = User(name=name, email=email, password=hashed)
    user.create()

    return user.__dict__
