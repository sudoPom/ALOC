import tkinter as tk
from view.frames.base_frame import BaseFrame


class SimpleDefinitionFrame(BaseFrame):
    def __init__(self, parent, controller, definition, re_render_func, **kwargs):
        self.__definition = definition
        super().__init__(parent, controller, self.get_bg_colour(),
                         self.get_button_text(), re_render_func, ** kwargs)

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_bg_colour())
        button.pack()
        self.__menu = tk.Menu(self, tearoff=0)
        definition_type_menu = tk.Menu(self.__menu, tearoff=0)
        definition_type_menu.add_command(label="Subject-Pair definition.",
                                         command=lambda: self.change_definition_type("subject pair"))
        definition_type_menu.add_command(label="Subject-Numerical-Pair definition.",
                                         command=lambda: self.change_definition_type("subject numerical pair"))

        self.__menu.add_cascade(
            label="Change definition type", menu=definition_type_menu)
        button.bind("<Button-1>", self.show_menu)

        info_label = tk.Label(self, text=self.get_definition_text(), font=(
            "Arial", 10), anchor=tk.W, justify=tk.LEFT)
        info_label.pack()

    def change_definition_type(self, type):
        self.get_controller().change_definition_type(self.__definition, type)
        self.trigger_re_render()

    def show_menu(self, event):
        self.__menu.tk_popup(event.x_root, event.y_root)

    def get_bg_colour(self):
        match self.__definition.get_type():
            case "subject pair":
                return "blue"
            case "subject numerical pair":
                return "green"
            case _:
                return "grey"

    def get_button_text(self):
        match self.__definition.get_type():
            case "subject pair":
                return "Subject Definition"
            case "subject numerical pair":
                return "Subject Numerical Definition"
            case _:
                return "Unknown Definition Type"

    def get_definition_text(self):
        match self.__definition.get_type():
            case "subject pair":
                return f"{self.__definition.get_subject()} is {self.__definition.get_other_subject()}"
            case "subject numerical pair":
                return f"{self.__definition.get_subject()} euqals {self.__definition.get_numerical_expression()}."
            case _:
                return "Unknown Definition Type! (Fix Mr Programmer!)"
