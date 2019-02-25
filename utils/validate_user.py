class Validate:

    @staticmethod
    def init_data(data):
        try:
            if not isinstance(data['national_id'], int):
                return {
                         'message': "national id should be numbers",
                         'status': 400
                       }

            return Validate.is_valid(
                firstname=data["firstname"],
                lastname=data["lastname"],
                othername=data["othername"],
                email=data["email"],
                isadmin=data["isadmin"],
                phone=data["phone"],
                passporturl=data["passporturl"],
                password=data["password"]
                )

        except KeyError as e:
            return {
                     'message': f"{e} field is required",
                     'status': 400
                   }

    @staticmethod
    def is_valid(**kwargs):
        '''checks if any required field is blank'''
        for key, val in kwargs.items():
            if val.strip() == '':
                return {
                         'message': f'{key} field cannot be blank',
                         'status': 400
                       }
