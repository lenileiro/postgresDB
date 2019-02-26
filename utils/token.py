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
            
            GoogPubKey = os.getenv("PRIVATE_KEY")     
            GoogPubKey = GoogPubKey.replace('-', '+')
            GoogPubKey = GoogPubKey.replace('_', '/')
            len(GoogPubKey) % 4  # 0
            secret_key = '-----BEGIN PRIVATE KEY-----\n' + GoogPubKey + '\n-----END PRIVATE KEY-----'
            
            token = jwt.encode(payload, secret_key, algorithm='RS256').decode('utf-8')
            print(f'jwt_token {payload}')
            return token

    @staticmethod
    def decode_token(token):
        secret_key = os.getenv("PRIVATE_KEY")
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload