from controllers.users import UsersController
from helpers.decorators import flask_request


class UsersApi(object):
    def __init__(self, request):
        self.request = request

    
    @flask_request
    def signup(self):
        return UsersController().signup(self.request.json)

    
    @flask_request
    def signout(self):
        return UsersController().signout()
    

    def login(self):
        return UsersController().login(self.request.json)

    
    @flask_request
    def save_user(self):
        return UsersController().save_user(self.request.json)


    @flask_request
    def save_user(self):
        return UsersController().save_user(self.request.json)


    @flask_request
    def get_users(self):
        return UsersController().get_users()
    

    
