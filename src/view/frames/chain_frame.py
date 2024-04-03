import tkinter as tk
from typing import Callable

from src.controller.controller import Controller
from src.model.components.chain_component import ChainComponent
from src.view.frames.simple_frame import SimpleFrame


class ChainFrame(SimpleFrame):
    """
    ChainFrame class represents the frame for displaying chain components in the GUI.

    Attributes:
    - parent (Canvas): The parent canvas.
    - controller (Controller): The controller managing component actions.
    - re_render_func (Callable): The function for re-rendering.
    - component (ChainComponent): The chain component to be displayed.

    Methods:
    - __init__(parent, controller, re_render_func, component): Initializes a ChainFrame object.
    - render(x, y): Renders the frame at the specified coordinates.
    """

    def __init__(
        self,
        parent: tk.Canvas,
        controller: Controller,
        re_render_func: Callable,
        component: ChainComponent,
    ):
        """
        Initializes a ChainFrame object.

        Args:
        - parent (Canvas): The parent canvas.
        - controller (Controller): The controller managing component actions.
        - re_render_func (Callable): The function for re-rendering.
        - component (ChainComponent): The chain component to be displayed.
        """
        super().__init__(
            parent,
            controller,
            re_render_func,
            component,
        )

    def create_widget(self):
        """
        Creates widgets for the frame.
        """
        button = tk.Button(
            self,
            text=self.get_component().get_form().get_display_text(),
            bg=self.get_component().get_form().get_colour(),
        )
        button.grid(row=0, column=0, sticky=tk.W)
        self.add_update_button()
        self.add_type_submenu()
        self.add_chain_options()
        self.add_delete_button()
        button.bind("<Button-1>", self.show_menu)

    def render(self, x: int, y: int) -> int:
        """
        Renders the frame at the specified coordinates.

        Args:
        - x (int): The x-coordinate.
        - y (int): The y-coordinate.

        Returns:
        - int: The y-coordinate after rendering.
        """
        current_component = self.get_component()
        assert isinstance(current_component, ChainComponent)
        y = super().render(x, y)
        next_component = current_component.get_next()
        if next_component:
            return ChainFrame(
                self.get_parent(),
                self.get_controller(),
                self.get_re_render_func(),
                next_component,
            ).render(x, y)
        return y

    def add_chain_options(self):
        """
        Adds options for chain components to the menu.
        """
        root_menu = self.get_menu()
        root_menu.add_command(
            label="Extend component", command=lambda: self.extend_component()
        )

    def extend_component(self):
        """
        Extends the associated component.
        """
        self.get_controller().extend_chain_component(
            self.get_component().get_internal_id()
        )
        self.trigger_re_render()

    def destruct(self):
        component = self.get_component()
        assert isinstance(component, ChainComponent)
        component.delete()
        self.get_controller().reset_ids()
        self.trigger_re_render()
