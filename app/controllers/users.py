
from datetime import datetime
from flask import  session
from models import UsersModel
import crypt


class UsersController(object):
    def __init__(self):
        self.users_model = UsersModel()


    # Create the user object
    def signup(self, user):
        user = {
            "name":user.get("name"),
            "email":user.get("email"),
            "password":crypt.crypt(user.get("password"), 'salt')
        }

        query = [{"$match": {"email": user["email"]}}]
        if self.users_model.get_information_users(query):
            raise Exception("email already exists")

        return self.users_model.insert(user)

    
    def login(self, user):

        response = { 
            "id": "d545f4ds",
            "name": "luis",
            "last_name": "Hernandez"
        }

        session['logged_in'] = True
        session['user'] = response
        return response

    
    def signout(self):
        return session.clear()


    def save_user(self, info):
        response = { 
                    "id": "d545f4ds",
                    "name": "luis",
                    "last_name": "Hernandez"
        }
        return response


    def get_users(self):
        response = [
            { "id": "d545f4ds","name": "luis","last_name": "Hernandez"},
            { "id": "d4f5ds4f","name": "Violetta","last_name": "Hernandez"}
        ]
        return response
    

    

