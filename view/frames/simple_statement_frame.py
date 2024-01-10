import tkinter as tk

from view.frames.base_frame import BaseFrame
from view.non_terminal_types import ContractNonTerminal


class SimpleStatementFrame(BaseFrame):
    def __init__(self, parent, controller, statement, re_render_func, **kwargs):
        self.__statement = statement
        super().__init__(
            parent,
            controller,
            self.get_bg_colour(),
            self.get_button_text(),
            re_render_func,
            component=statement,
            **kwargs,
        )

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_bg_colour())
        button.grid(row=0, column=0, sticky=tk.W)
        self.add_type_submenu()
        self.add_chain_options()
        self.add_update_button()
        self.add_delete_button()
        button.bind("<Button-1>", self.show_menu)

    def destruct(self):
        self.get_controller().delete_non_definition_component(self.__statement.get_id())
        self.trigger_re_render()

    def validate_entry(self, entry, entry_type):
        ContractNonTerminal.validate_entry(entry, entry_type)

    def get_bg_colour(self):
        match self.__statement.get_type():
            case "subject modal":
                return "yellow"
            case "subject date":
                return "orange"
            case "date subject":
                return "purple"
            case _:
                return "grey"

    def get_button_text(self):
        match self.__statement.get_type():
            case "subject modal":
                return "Subject Modal Statement"
            case "subject date":
                return "Subject Date Statement"
            case "date subject":
                return "Date Subject Statement"
            case _:
                return "Unknown Statement Type!"
