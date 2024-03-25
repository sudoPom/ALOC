import tkinter as tk
from abc import abstractmethod
from typing import Callable

from src.controller.controller import Controller
from src.model.components.component import Component


class BaseFrame(tk.Frame):
    def __init__(
        self,
        parent: tk.Canvas,
        controller: Controller,
        re_render_func: Callable,
        component: Component,
        **kwargs,
    ):
        """
        Initializes a BaseFrame object.

        Args:
        - parent (tk.Widget): The parent widget.
        - controller (Controller): The controller managing component actions.
        - re_render_func (Callable): The function for re-rendering.
        - component (Component): The component associated with the frame.
        - render_settings (set): The settings for rendering the frame.
        - **kwargs: Additional keyword arguments.
        """
        super().__init__(parent, **kwargs)
        self.__parent = parent
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.__menu = tk.Menu(self, tearoff=0)
        self.__component = component
        self.create_widget()

    @abstractmethod
    def create_widget(self):
        """
        Creates the widget for this frame.
        """

    def get_controller(self) -> Controller:
        """
        Returns the controller.

        Returns:
        - Controller: The controller managing component actions.
        """
        return self.__controller

    def get_component(self) -> Component:
        """
        Returns the component.

        Returns:
        - Component: The component associated with the frame.
        """
        return self.__component

    def get_re_render_func(self) -> Callable:
        """
        Returns the re-render function.

        Returns:
        - Callable: The function for re-rendering.
        """
        return self.__re_render_func

    def get_parent(self) -> tk.Canvas:
        """
        Returns the parent widget.

        Returns:
        - tk.Widget: The parent widget.
        """
        return self.__parent

    def get_menu(self) -> tk.Menu:
        """
        Returns the associated menu.

        Returns:
        - tk.Menu: The associated menu.
        """
        return self.__menu

    def trigger_re_render(self):
        """
        Triggers re-rendering of the frame.
        """
        self.__re_render_func()

    def show_menu(self, event):
        """
        Displays the associated menu.

        Args:
        - event: The event that triggered the menu.
        """
        self.__menu.tk_popup(event.x_root, event.y_root)

    def change_component_type(self, component_type):
        """
        Changes the type of the associated component.

        Args:
        - component_type: The new type of the component.
        """
        Controller.change_component_type(self.__component, component_type)
        self.trigger_re_render()

    def add_delete_button(self):
        """
        Adds a delete button to the menu.
        """
        self.__menu.add_command(label="Delete", command=self.destruct)

    def destruct(self):
        """
        Deletes the associated component.
        """
        self.__controller.delete_component(self.__component.get_internal_id())
        self.trigger_re_render()

    def add_type_submenu(self):
        """
        Adds a submenu for changing the component type.
        """
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

    def get_display_text(self):
        """
        Returns the display text of the associated component.

        Returns:
        - str: The display text.
        """
        return self.__component.get_display_text()

    def render(self, x, y):
        """
        Renders the frame at the specified coordinates.

        Args:
        - x: The x-coordinate.
        - y: The y-coordinate.

        Returns:
        - int: The required height of the frame.
        """
        display_text = self.get_display_text()
        self.__parent.create_window(x, y, anchor=tk.NW, window=self)
        self.__parent.update()
        if not display_text:
            return self.winfo_reqheight()
        label = tk.Message(self, font=("Arial", 10), text=display_text, width=500)
        label.grid(row=1, column=0, sticky=tk.W)
        self.__parent.update()
        return self.winfo_reqheight()
