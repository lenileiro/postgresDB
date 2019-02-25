import os
import jwt
from datetime import datetime, timedelta


class Token:
    @staticmethod
    def generate_token(**kwargs):
        for key, val in kwargs.items():
            payload = {
                key: val,
                'exp': datetime.utcnow()+ timedelta(minutes=6000),
                'iat': datetime.utcnow()}

            secret_key = "asdfg"
            token = jwt.encode(payload, str(secret_key), algorithm='HS256')
            return token.decode()

    @staticmethod
    def decode_token(token):
        secret_key = "asdfg"
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload