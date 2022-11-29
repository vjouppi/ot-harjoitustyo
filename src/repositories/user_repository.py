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
        self.userlist.append(user)
