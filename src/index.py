from tkinter import Tk
from ui.ui import UI


def main():
    mywindow = Tk()
    mywindow.title("Freezer database")
    myview = UI(mywindow)
    myview.show_login()

    mywindow.mainloop()


if __name__ == "__main__":
    main()
