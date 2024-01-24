import tkinter as tk


class ContractFrame(tk.Frame):
    def __init__(self, parent, controller, re_render_func, **kwargs):
        super().__init__(parent, **kwargs)
        self.__parent = parent
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.__menu = tk.Menu(self, tearoff=0)
        self.create_widgets()

    def create_widgets(self):
        button = tk.Button(self, text="Contract", bg="red")
        button.pack()
        self.__menu = tk.Menu(self, tearoff=0)
        self.__menu.add_command(
            label="Add Definition", command=lambda: self.add_new_component("definition")
        )
        self.__menu.add_command(
            label="Add Statement",
            command=lambda: self.add_new_component("statement"),
        )
        self.__menu.add_command(
            label="Add Conditional Definition",
            command=lambda: self.add_new_component("conditional_definition"),
        )
        self.__menu.add_command(
            label="Add Conditional Statement",
            command=lambda: self.add_new_component("conditional_statement"),
        )
        button.bind("<Button-1>", self.show_menu)

    def show_menu(self, event):
        self.__menu.tk_popup(event.x_root, event.y_root)

    def add_new_component(self, component_name):
        self.__controller.add_new_component(component_name)
        self.__re_render_func()

    def render(self, x, y):
        self.__parent.create_window(x, y, anchor=tk.NW, window=self)
        self.__parent.update()
        y += self.winfo_reqheight()
        return y
