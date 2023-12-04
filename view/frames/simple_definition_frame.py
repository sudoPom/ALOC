import tkinter as tk
from view.frames.base_frame import BaseFrame
from controller.controller import Controller
from view.non_terminal_types import ContractNonTerminal


class SimpleDefinitionFrame(BaseFrame):
    def __init__(self, parent, controller, definition, re_render_func, **kwargs):
        self.__definition = definition
        super().__init__(parent, controller, self.get_bg_colour(),
                         self.get_button_text(), re_render_func, component=definition, **kwargs)

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_bg_colour())
        button.pack()
        self.add_menu()
        self.add_type_submenu()
        self.add_update_button()
        self.add_delete_button()

        button.bind("<Button-1>", self.show_menu)

        info_label = tk.Label(self, text=self.__definition.get_display_text(), font=(
            "Arial", 10), anchor=tk.W, justify=tk.LEFT)
        info_label.pack()

    def change_definition_type(self, type):
        Controller.change_component_type(self.__definition, type)
        self.trigger_re_render()

    def destruct(self):
        self.get_controller().delete_definition(self.__definition.get_id())
        self.trigger_re_render()

    def validate_entry(self, entry, entry_type):
        match entry_type:
            case ContractNonTerminal.SUBJECT:
                return ContractNonTerminal.validate_subject(entry)
            case ContractNonTerminal.NUMERICAL_EXPRESSION:
                return ContractNonTerminal.validate_numerical_expression(entry)
            case _:
                raise ValueError(f"Invalid expression: {entry}")

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
