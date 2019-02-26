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
            
            secret_key = Token.private_secret_key()
            token = jwt.encode(payload, secret_key, algorithm='RS256').decode('utf-8')
            print(f'jwt_token {payload}')
            return token

    @staticmethod
    def decode_token(token):
        secret_key = Token.public_secret_key()
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    

    @staticmethod
    def private_secret_key():
        GoogPubKey = os.getenv("PRIVATE_KEY")     
        GoogPubKey = GoogPubKey.replace('-', '+')
        GoogPubKey = GoogPubKey.replace('_', '/')
        len(GoogPubKey) % 4  # 0
        secret_key = '-----BEGIN PRIVATE KEY-----\n' + GoogPubKey + '\n-----END PRIVATE KEY-----'
        return secret_key
    
    @staticmethod
    def public_secret_key():
        GoogPubKey = os.getenv("PUBLIC_KEY")     
        GoogPubKey = GoogPubKey.replace('-', '+')
        GoogPubKey = GoogPubKey.replace('_', '/')
        len(GoogPubKey) % 4  # 0
        secret_key = '-----BEGIN PUBLIC KEY-----\n' + GoogPubKey + '\n-----END PUBLIC KEY-----'
        return secret_key
            
        
