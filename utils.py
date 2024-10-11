import jwt
import datetime
from datetime import timedelta

def generate_jwt(payload, secret_key, expires_delta: timedelta):
    payload['exp'] = datetime.datetime.utcnow() + expires_delta
    return jwt.encode(payload, secret_key, algorithm="HS256")

def verify_jwt(token, secret_key):
    return jwt.decode(token, secret_key, algorithms=["HS256"])
