import ast
class Helper:
    @staticmethod
    def format_create_account_response(iterable):
        user = {
                    "national_id": iterable[1],
                    "firstname": iterable[2],
                    "lastname": iterable[3],
                    "othername": iterable[4],
                    "phone": iterable[6],
                    "email": iterable[5],
                    "isadmin": ast.literal_eval(iterable[7]),
                    "passporturl": iterable[9]
                }
        return user