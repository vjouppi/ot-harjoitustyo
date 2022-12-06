from tkinter import ttk, StringVar, constants
from entities.user import User
from repositories.user_repository import UserRepository


class UI:
    def __init__(self, root):
        self.root = root
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.userrepo = UserRepository()

    def do_login(self):
        myuser = User(self.username_entry.get(), self.password_entry.get())
        found_user = self.userrepo.find_user(myuser.username)
        if found_user:
            if found_user.password == myuser.password:
                self.show_main()

    def do_newuser(self):
        myuser = User(self.username_entry.get(), self.password_entry.get())
        found_user = self.userrepo.find_user(myuser.username)
        if not found_user:
            try:
                self.userrepo.create(myuser)
                status_label = ttk.Label(master=self.frame, text="User created successfully")
            except:
                status_label = ttk.Label(master=self.frame, text="User creation failed")
            status_label.grid(padx=10, pady=10, column=1, row=4, columnspan=2, sticky=constants.EW)
        else:
            status_label = ttk.Label(master=self.frame, text="User already exists")
            status_label.grid(padx=10, pady=10, column=1, row=4, columnspan=2, sticky=constants.EW)

    def show_main(self):
        if self.frame:
            self.frame.destroy()
        self.frame = ttk.Frame(master=self.root)
        success_label = ttk.Label(master=self.frame, text="Login successful")
        success_label.grid(padx=10, pady=10, sticky=constants.EW)
        self.frame.pack()

    def show_login(self):
        self.frame = ttk.Frame(master=self.root)

        username_label = ttk.Label(master=self.frame, text="Username")

        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(padx=10, pady=10, column=1,
                            row=1, sticky=constants.W)
        self.username_entry.grid(
            padx=10, pady=10, column=2, row=1, sticky=constants.E)

        password_label = ttk.Label(master=self.frame, text="Password")

        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(padx=10, pady=10, column=1,
                            row=2, sticky=constants.W)
        self.password_entry.grid(
            padx=10, pady=10, column=2, row=2, sticky=constants.E)

        login_button = ttk.Button(
            master=self.frame,
            text="Login",
            command=self.do_login
        )

        create_user_button = ttk.Button(
            master=self.frame,
            text="Create user",
            command=self.do_newuser
        )

        login_button.grid(padx=10, pady=10, column=1,
                          row=3, sticky=constants.W)
        create_user_button.grid(
            padx=10, pady=10, column=2, row=3, sticky=constants.E)

        self.frame.pack()
