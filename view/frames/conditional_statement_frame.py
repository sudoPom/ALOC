import tkinter as tk

from view.frames.base_frame import BaseFrame


class ConditionalStatementFrame(BaseFrame):
    def __init__(
        self, parent, controller, conditional_statement, re_render_func, **kwargs
    ):
        self.__conditional_statement = conditional_statement
        super().__init__(
            parent,
            controller,
            self.get_bg_colour(),
            self.get_button_text(),
            re_render_func,
            component=conditional_statement,
            **kwargs,
        )

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_bg_colour())
        button.grid(row=0, column=0, sticky=tk.W)
        self.add_type_submenu()
        self.add_delete_button()
        button.bind("<Button-1>", self.show_menu)

    def destruct(self):
        self.get_controller().delete_non_definition_component(
            self.__conditional_statement.get_id()
        )
        self.trigger_re_render()

    def get_bg_colour(self):
        return "teal"

    def get_button_text(self):
        match self.__conditional_statement.get_type():
            case "if":
                return "If Conditional Statement"
            case "if_then":
                return "If Then Conditional Statement"
            case _:
                return "Unknown conditional_statement Type!"
