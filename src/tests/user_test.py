import unittest

from entities.user import User
from repositories.user_repository import UserRepository


class testUser(unittest.TestCase):
    def setUp(self):
        self.userrepo = UserRepository()

    def test_create_user(self):
        newuser = User("a", "b")
        self.userrepo.create(newuser)
        self.assertEqual(str("a"), str(self.userrepo.find_user("a")))
