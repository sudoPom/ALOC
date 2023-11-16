import tkinter as tk
from tkinter import simpledialog

class ContractButton(tk.Frame):
    def __init__(self, parent, controller, re_render_func, **kwargs):
        super().__init__(parent, **kwargs)
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.create_widgets()

    def create_widgets(self):
        button = tk.Button(self, text="Contract", bg="red")
        button.pack()
        self.__menu = tk.Menu(self, tearoff=0)
        definition_menu = tk.Menu(self.__menu, tearoff=0)
        definition_menu.add_command(label="Add subject pair definition.", command=lambda: self.add_new_definition("subject pair"))
        definition_menu.add_command(label="Add subject numerical pair definition.", command=lambda: self.add_new_definition("subject numerical pair"))
        self.__menu.add_cascade(label="Add definition", menu=definition_menu)
        self.__menu.add_separator()
        self.__menu.add_command(label="Close", command=self.menu_close)
        button.bind("<Button-1>", self.show_menu)

    def open_definition_selection_menu(self):
        menu = tk.Menu(self.__menu, tearoff=0)
        menu.add_command(label="Add subject pair definition.", command=lambda: self.add_new_definition("subject pair"))
        menu.add_command(label="Add subject numerical pair definition.", command=lambda: self.add_new_definition("subject numerical pair"))
        self.__menu.entryconfig("Add definition", menu=menu)

    def add_new_definition(self, definition_type):
        self.__controller.add_new_definition(definition_type)
        self.__re_render_func()

    def menu_close(self):
        self.__menu.unpost()

    def show_menu(self, event):
        self.__menu.post(event.x_root, event.y_root)
    

class SimpleDefinitionButton(tk.Frame):
    def __init__(self, parent, definition, re_render_func, **kwargs):
        super().__init__(parent, **kwargs)
        self.__definition = definition
        self.__re_render_func = re_render_func
        self.create_widgets()

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_bg_colour())
        button.pack()
        self.__menu = tk.Menu(self, tearoff=0)
        self.__menu.add_command(label="Menu Option 1", command=self.menu_option_1)
        self.__menu.add_command(label="Menu Option 2", command=self.menu_option_2)
        self.__menu.add_separator()
        self.__menu.add_command(label="Close", command=self.menu_close)
        button.bind("<Button-1>", self.show_menu)

    def menu_option_1(self):
        print("Definition Button Menu Item 1!")

    def menu_option_2(self):
        print("Definition Button Menu Item 2!")

    def menu_close(self):
        self.__menu.unpost()

    def show_menu(self, event):
        self.__menu.post(event.x_root, event.y_root)

    def get_bg_colour(self):
        match self.__definition.get_type():
            case "subject pair":
                return "blue"
            case "subject numerical pair":
                return "green"
            case _:
                return "grey"

    def get_text(self):
        match self.__definition.get_type():
            case "subject pair":
                return "Subject Definition"
            case "subject numerical pair":
                return "Subject Numerical Definition"
            case _:
                return "Unknown Definition Type"
            

