import tkinter as tk

class ContractFrame(tk.Frame):
    def __init__(self, parent, contract, **kwargs):
        super().__init__(parent, **kwargs)
        self.contract = contract
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Contract", bg="red")
        label.pack()

class SimpleDefinitionFrame(tk.Frame):
    def __init__(self, parent, definition, **kwargs):
        super().__init__(parent, **kwargs)
        self.definition = definition
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Simple Definition", bg="blue")
        label.pack()
