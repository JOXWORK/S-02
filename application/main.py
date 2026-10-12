from tkinter import Tk


class App:
    def __init__(self):
        self.root = Tk()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
