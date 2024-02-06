from tkinter import Canvas
from typing import Callable

from controller.controller import Controller
from model.components.chain_component import ChainComponent
from view.frames.base_frame import BaseFrame


class ChainFrame(BaseFrame):
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
        parent: Canvas,
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
            {"updatable", "deletable", "chain_component", "multi-typed"},
        )

    def render(self, x: int, y: int) -> int:
        """
        Renders the frame at the specified coordinates.

        Args:
        - x (int): The x-coordinate.
        - y (int): The y-coordinate.

        Returns:
        - int: The y-coordinate after rendering.
        """
        current_component: ChainComponent = self.get_component()
        y += super().render(x, y)
        current_component = current_component.get_next_component()
        while current_component:
            y += BaseFrame(
                self.get_parent(),
                self.get_controller(),
                self.get_re_render_func(),
                current_component,
                {"updatable", "multi-typed", "deletable", "chain_component"},
            ).render(x, y)
            current_component = current_component.get_next_component()
        return y
