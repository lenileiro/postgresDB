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

            secret_key = os.getenv("PRIVATE_KEY")
            token = jwt.encode(payload, str(secret_key), algorithm='RS256').decode('utf-8')
            return token

    @staticmethod
    def decode_token(token):
        secret_key = os.getenv("PRIVATE_KEY")
        payload = jwt.decode(token, secret_key, algorithms=['RS256'])
        return payload