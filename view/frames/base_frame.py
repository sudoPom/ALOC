import tkinter as tk

from controller.controller import Controller
from view.update_menu_handler import UpdateFormHandler


class BaseFrame(tk.Frame):
    def __init__(
        self,
        parent,
        controller,
        re_render_func,
        component,
        render_settings,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self.__parent = parent
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.__menu = tk.Menu(self, tearoff=0)
        self.__component = component
        self.__widget_handler = UpdateFormHandler()
        self.__render_settings = render_settings
        self.create_widgets()

    def create_widgets(self):
        button = tk.Button(
            self,
            text=self.__component.get_type().get_display_text(),
            bg=self.__component.get_type().get_colour(),
        )
        button.grid(row=0, column=0, sticky=tk.W)
        if "updatable" in self.__render_settings:
            self.add_update_button()
        if "multi-typed" in self.__render_settings:
            self.add_type_submenu()
        if "chain_component" in self.__render_settings:
            self.add_chain_options()
        if "deletable" in self.__render_settings:
            self.add_delete_button()
        button.bind("<Button-1>", self.show_menu)

    def get_controller(self):
        return self.__controller

    def get_component(self):
        return self.__component

    def get_re_render_func(self):
        return self.__re_render_func

    def get_parent(self):
        return self.__parent

    def get_menu(self):
        return self.__menu

    def trigger_re_render(self):
        self.__re_render_func()

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
        self.__controller.delete_component(self.__component.get_id())
        self.trigger_re_render()

    def add_update_button(self):
        self.__menu.add_command(
            label="Update",
            command=lambda: self.__widget_handler.create_update_form(
                self, self.__component, self.__re_render_func, self.__controller
            ),
        )

    def add_type_submenu(self):
        menu = tk.Menu(self.__menu, tearoff=0)
        type_names = [
            type_spec.get_name() for type_spec in self.__component.get_types()
        ]
        for type_name in type_names:
            menu.add_command(
                label=type_name,
                command=lambda c_type=type_name: self.change_component_type(c_type),
            )
        self.__menu.add_cascade(label="Change component type", menu=menu)

    def add_chain_options(self):
        menu = tk.Menu(self.__menu, tearoff=0)
        menu.add_command(
            label="Extend component", command=lambda: self.extend_component()
        )
        self.__menu.add_cascade(label="Component chain options...", menu=menu)

    def get_display_text(self):
        return self.__component.get_display_text()

    def render(self, x, y):
        display_text = self.get_display_text()
        self.__parent.create_window(x, y, anchor=tk.NW, window=self)
        self.__parent.update()
        if not display_text:
            return self.winfo_reqheight()
        label = tk.Message(self, font=("Arial", 10), text=display_text, width=500)
        label.grid(row=1, column=0, sticky=tk.W)
        self.__parent.update()
        return self.winfo_reqheight()
