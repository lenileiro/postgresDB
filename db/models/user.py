from datetime import datetime
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from ..model import Base
from utils.validate_user import Validate as vl

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
                return {
                     'message': Base.get('user', national_id=national_id),
                     'status': 201
                   }
            else:
                return error