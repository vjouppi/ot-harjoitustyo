class User:
    """ A class for describing users.

    Attributes:
      username: String, user id
      password: String, user password
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username
