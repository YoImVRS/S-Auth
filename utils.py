from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_password(password):
    return ph.hash(password)

def verify_password(hashed_password, plain_password):
    try:
        return ph.verify(hashed_password, plain_password)
    except:
        return False
