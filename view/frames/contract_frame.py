import tkinter as tk

from view.frames.base_frame import BaseFrame


class ContractFrame(BaseFrame):
    def __init__(self, parent, controller, re_render_func, **kwargs):
        super().__init__(
            parent, controller, "red", "Contract", re_render_func, **kwargs
        )

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_colour())
        button.pack()
        self.__menu = tk.Menu(self, tearoff=0)
        definition_menu = tk.Menu(self.__menu, tearoff=0)
        definition_menu.add_command(
            label="Add subject pair definition.",
            command=lambda: self.add_new_definition("subject pair"),
        )
        definition_menu.add_command(
            label="Add subject numerical pair definition.",
            command=lambda: self.add_new_definition("subject numerical pair"),
        )
        statement_menu = tk.Menu(self.__menu, tearoff=0)
        statement_menu.add_command(
            label="Add subject modal statement.",
            command=lambda: self.add_new_statement("subject modal"),
        )
        statement_menu.add_command(
            label="Add subject date statement.",
            command=lambda: self.add_new_statement("subject date"),
        )
        statement_menu.add_command(
            label="Add date subject statement.",
            command=lambda: self.add_new_statement("date subject"),
        )
        conditional_statement_menu = tk.Menu(self.__menu, tearoff=0)
        conditional_statement_menu.add_command(
            label='Add "If" conditional statement',
            command=lambda: self.add_new_conditional_statement("if"),
        )
        conditional_statement_menu.add_command(
            label='Add "If-Then" conditional statement',
            command=lambda: self.add_new_conditional_statement("if_then"),
        )
        conditional_definition_menu = tk.Menu(self.__menu, tearoff=0)
        conditional_definition_menu.add_command(
            label='Add "If" conditional definition',
            command=lambda: self.add_new_conditional_definition("if"),
        )
        conditional_definition_menu.add_command(
            label='Add "If-Then" conditional definition',
            command=lambda: self.add_new_conditional_definition("if_then"),
        )
        self.__menu.add_cascade(label="Add definition", menu=definition_menu)
        self.__menu.add_cascade(label="Add statement", menu=statement_menu)
        self.__menu.add_cascade(
            label="Add conditional statement", menu=conditional_statement_menu
        )
        self.__menu.add_cascade(
            label="Add conditional definition", menu=conditional_definition_menu
        )
        button.bind("<Button-1>", self.show_menu)

    def show_menu(self, event):
        self.__menu.tk_popup(event.x_root, event.y_root)

    def add_new_definition(self, definition_type):
        self.get_controller().add_new_definition(definition_type)
        self.trigger_re_render()

    def add_new_statement(self, statement_type):
        self.get_controller().add_new_statement(statement_type)
        self.trigger_re_render()

    def add_new_conditional_statement(self, conditional_statement_type):
        self.get_controller().add_new_conditional_statement(conditional_statement_type)
        self.trigger_re_render()

    def add_new_conditional_definition(self, conditional_definition_type):
        self.get_controller().add_new_conditional_definition(
            conditional_definition_type
        )
        self.trigger_re_render()
