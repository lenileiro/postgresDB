from datetime import datetime
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from ..model import Base
from utils.validate_user import Validate as vl
from utils.token import Token
from utils.helper import Helper

class UserModel:
    
    @staticmethod
    def insert_user(params):
            error = vl.init_data(params)
            if not error:
                created_at = '%s' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                hashed_pwd = generate_password_hash(params["password"])

                national_id = Base.insert(
                'user',
                national_id=params["national_id"],
                firstname=params["firstname"],
                lastname=params["lastname"],
                othername=params["othername"],
                email=params["email"],
                isadmin=params["isadmin"],
                phone=params["phone"],
                passporturl=params["passporturl"],
                password=hashed_pwd,
                created_at=created_at
                )

                token = Token.generate_token(
                national_id=params["national_id"],
                isadmin=params["isadmin"])

                data = Base.get('user', national_id=national_id)
                user = Helper.format_create_account_response(data)

                response = { 
                    "status":201,
                    "data": {
                        "token": token,
                        "user": user
                        }
                }
                return response
            else:
                return error
    