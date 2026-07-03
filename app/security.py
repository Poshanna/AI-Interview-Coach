import bcrypt

# Hash password
def hash_password(password: str):
    # Encode password as bytes, salt, then hash
    bytes_pw = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes_pw, salt)
    return hashed.decode('utf-8')

# Verify password
def verify_password(plain_password: str, hashed_password: str):
    bytes_pw = plain_password.encode('utf-8')
    bytes_hash = hashed_password.encode('utf-8')
    return bcrypt.checkpw(bytes_pw, bytes_hash)