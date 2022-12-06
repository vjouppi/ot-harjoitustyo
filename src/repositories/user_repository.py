class UserError(Exception):
    pass

class UserRepository:

    def __init__(self):
        self.userlist = []

    def list_users(self):
        return self.userlist

    def find_user(self, username):
        for user in self.userlist:
            if user.username == username:
                return user
        return None

    def create(self, user):
        if user.username == "":
            raise UserError("Username can't be empty")
        else:
            self.userlist.append(user)
