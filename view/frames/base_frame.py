import tkinter as tk

from controller.controller import Controller
from view.update_menu_handler import UpdateFormHandler


class BaseFrame(tk.Frame):
    def __init__(
        self,
        parent,
        controller,
        colour,
        button_text,
        re_render_func,
        component=None,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.__colour = colour
        self.__text = button_text
        self.__menu = tk.Menu(self, tearoff=0)
        self.__component = component
        self.__widget_handler = UpdateFormHandler()
        self.create_widgets()

    def get_text(self):
        return self.__text

    def get_colour(self):
        return self.__colour

    def get_controller(self):
        return self.__controller

    def get_menu(self):
        return self.__menu

    def trigger_re_render(self):
        self.__re_render_func()

    def create_widgets(self):
        raise NotImplementedError(
            "Base class method for create_widgets should be overridden"
        )

    def show_menu(self, event):
        self.__menu.tk_popup(event.x_root, event.y_root)

    def change_component_type(self, component_type):
        Controller.change_component_type(self.__component, component_type)
        self.trigger_re_render()

    def extend_component(self):
        Controller.extend_component_chain(self.__component)
        self.trigger_re_render()

    def add_delete_button(self):
        self.__menu.add_command(label="Delete", command=self.destruct)

    def destruct(self):
        raise NotImplementedError(
            "Base Frame Destruct (delete) method should be overridden."
        )

    def add_update_button(self):
        self.__menu.add_command(
            label="Update",
            command=lambda: self.__widget_handler.create_update_form(
                self, self.__component, self.__re_render_func, self.__controller
            ),
        )

    def add_type_submenu(self):
        menu = tk.Menu(self.__menu, tearoff=0)
        for component_type in self.__component.get_types():
            menu.add_command(
                label=component_type,
                command=lambda c_type=component_type: self.change_component_type(
                    c_type
                ),
            )
        self.__menu.add_cascade(label="Change component type", menu=menu)

    def add_chain_options(self):
        menu = tk.Menu(self.__menu, tearoff=0)
        menu.add_command(
            label="Extend component", command=lambda: self.extend_component()
        )
        self.__menu.add_cascade(label="Component chain options...", menu=menu)
