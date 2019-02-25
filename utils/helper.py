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
                    "isadmin": iterable[7],
                    "passporturl": iterable[9],
                    "created_at": iterable[10].strftime("%Y-%m-%d %H:%M:%S")
                }
        return user