import tkinter as tk

from controller.controller import Controller
from model.model import Model
from view.view import View


class App:
    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.controller)

    def main_loop(self):
        self.view.mainloop()


if __name__ == "__main__":

    app = App()
    app.main_loop()
