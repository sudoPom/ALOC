import tkinter as tk
from model.model import Model
from view.view import View
from controller.controller import Controller

class App:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.view = View(root)
        self.controller = Controller(self.model, self.view)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
