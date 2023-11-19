import tkinter as tk
from view.frames.base_frame import BaseFrame


class ContractFrame(BaseFrame):
    def __init__(self, parent, controller, re_render_func, **kwargs):
        super().__init__(parent, controller, "red", "Contract", re_render_func, **kwargs)

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_colour())
        button.pack()
        self.__menu = tk.Menu(self, tearoff=0)
        definition_menu = tk.Menu(self.__menu, tearoff=0)
        definition_menu.add_command(label="Add subject pair definition.",
                                    command=lambda: self.add_new_definition("subject pair"))
        definition_menu.add_command(label="Add subject numerical pair definition.",
                                    command=lambda: self.add_new_definition("subject numerical pair"))
        self.__menu.add_cascade(label="Add definition", menu=definition_menu)
        self.__menu.add_separator()
        self.__menu.add_command(label="Close", command=self.menu_close)
        button.bind("<Button-1>", self.show_menu)

    def show_menu(self, event):
        self.__menu.tk_popup(event.x_root, event.y_root)

    def add_new_definition(self, definition_type):
        self.get_controller().add_new_definition(definition_type)
        self.trigger_re_render()
