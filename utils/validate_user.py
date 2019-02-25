import re
from db.model import Base
class Validate:

    @staticmethod
    def init_data(data):
        try:
            if not isinstance(data['national_id'], int):
                return {
                         'message': 'national id should be numbers',
                         'status': 400
                       }

            if not isinstance(data['isadmin'], bool):
                return {
                         'message': 'isadmin should be a boolean',
                         'status': 400
                       }
            if Validate.is_email_valid(email=data["email"]):
                return {
                        'message': 'email format is invalid',
                        'status': 400
                       }

            if Validate.check_password_format(password=data["password"]):
                   return {
                            'message': 'Password should more than 8 characters and less than 20',
                            'status': 401
                          }

            if Validate.check_if_user_exists(data['national_id']):
                return {
                    'message': 'The user already exists',
                    'status': 409
                   }
                   
            return Validate.is_not_blank(
                firstname=data['firstname'],
                lastname=data['lastname'],
                othername=data['othername'],
                email=data['email'],
                phone=data['phone'],
                passporturl=data['passporturl'],
                password=data['password']
                )

        except KeyError as e:
            return {
                     'message': f'{e} field is required',
                     'status': 400
                   }
        
        
    @staticmethod
    def is_not_blank(**kwargs):
        """checks if any required field is blank"""
        for key, val in kwargs.items():
            if val.strip() == '':
                return {
                         'message': f'{key} field cannot be blank',
                         'status': 400
                       }
    @staticmethod
    def check_password_format(password):
        if len(password) < 5 or len(password) > 20:
            return True

    @staticmethod
    def is_email_valid(email):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            return True
    
    @staticmethod
    def check_if_user_exists(national_id):
        user = Base.get('user', national_id=national_id)
        return user