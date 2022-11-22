from entities.user import User
from repositories.user_repository import UserRepository

def main():
    print("le main routine")
    userrepo = UserRepository()
    myuser = User("jaakko","passu")
    userrepo.create(myuser)
    for user in userrepo.list_users():
        print(user)

if __name__ == "__main__":
    main()
