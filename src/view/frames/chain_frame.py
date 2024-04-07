import tkinter as tk
from typing import Callable

from src.controller.controller import Controller
from src.model.components.chain_component import ChainComponent
from src.view.frames.simple_frame import SimpleFrame


class ChainFrame(SimpleFrame):
    """
    Widget for interacting with a SimpleFrame

    Args:
        parent (:obj:`tk.Canvas`): The parent canvas.
        controller (:obj:`Controller`): The controller managing component actions.
        re_render_func (:obj:`Callable`): The function for re-rendering.
        component (:obj:`ChainComponent`): The component associated with the frame.
    """

    def __init__(
        self,
        parent: tk.Canvas,
        controller: Controller,
        re_render_func: Callable,
        component: ChainComponent,
    ):
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
            x: The x-coordinate to render the widget on the canvas.
            y: The y-coordinate to render the widget on the canvas.

        Returns:
            int: The height of the frame on the canvas.
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
        """
        Deletes the associated component.
        """
        component = self.get_component()
        assert isinstance(component, ChainComponent)
        component.delete()
        self.get_controller().reset_ids()
        self.trigger_re_render()
