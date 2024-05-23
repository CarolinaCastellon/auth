import bcrypt


def hash_password(password: bytes) -> bytes:
    return bcrypt.hashpw(password, bcrypt.gensalt())


def verify_password(password: bytes, hashed: bytes) -> bool:
    return bcrypt.checkpw(password, hashed)
