import json
from db.models.user import UserModel
from test.base import BaseTest


class TestPostRequest(BaseTest):

    def test_account_creation(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 201)
    
    def test_exist_account_creation(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        UserModel.insert_user(user)
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 409)
        self.assertIsInstance(response["message"], str)
    
    def test_account_creation_missing_field(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 400)
        self.assertIsInstance(response["message"], str)

    def test_account_creation_blank_value(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "     ",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 400)
        self.assertIsInstance(response["message"], str)
    
    def test_account_creation_string_national_id(self):
        user = {
                "national_id": "32308961",
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 400)
        self.assertIsInstance(response["message"], str)
    
    def test_account_creation_invalid_email(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoegmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 400)
        self.assertIsInstance(response["message"], str)

    def test_account_creation_invalid_password(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "----",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 401)
        self.assertIsInstance(response["message"], str)