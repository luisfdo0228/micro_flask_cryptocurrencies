from models.connection import Manager


class UsersModel(Manager):
    def __init__(self):
        self.collection = "users_information"

    def get_information_users(self, query):
        if not isinstance(query, list):
            return {}
        return self.execute(query)
