import tkinter as tk

from controller.controller import Controller
from model.model import Model


class App:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.controller = Controller(self.model)

if __name__ == "__main__":

    root = tk.Tk()
    app = App(root)
    root.mainloop()
