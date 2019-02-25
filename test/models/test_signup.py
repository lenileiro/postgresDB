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
                "isadmin": True,
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        result = UserModel.insert_user(user)
        self.assertEqual(result["status"], 201)
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["data"]["token"], str)
        self.assertIsInstance(result["data"]["user"], dict)
        self.assertIsInstance(result["data"]["user"]["national_id"], int)
        self.assertIsInstance(result["data"]["user"]["firstname"], str)
        self.assertIsInstance(result["data"]["user"]["lastname"], str)
        self.assertIsInstance(result["data"]["user"]["othername"], str)
        self.assertIsInstance(result["data"]["user"]["email"], str)
        self.assertIsInstance(result["data"]["user"]["phone"], str)
        self.assertIsInstance(result["data"]["user"]["passporturl"], str)
        self.assertIsInstance(result["data"]["user"]["isadmin"], bool)
    
    def test_exist_account_creation(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": False,
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
                "isadmin": False,
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
                "isadmin": False,
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
                "isadmin": False,
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
                "isadmin": False,
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
                "isadmin": False,
                "phone": "+254724862149",
                "password": "----",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = UserModel.insert_user(user)
        self.assertEqual(response["status"], 401)
        self.assertIsInstance(response["message"], str)