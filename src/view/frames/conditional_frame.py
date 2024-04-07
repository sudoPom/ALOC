import tkinter as tk

from src.model.components.conditional_component import ConditionalComponent
from src.view.constants import Constants
from src.view.frames.base_frame import BaseFrame
from src.view.frames.chain_frame import ChainFrame


class ConditionalFrame(BaseFrame):
    """
    Widget for interacting with a ConditionalComponent

    Args:
        parent (:obj:`tk.Canvas`): The parent canvas.
        controller (:obj:`Controller`): The controller managing component actions.
        re_render_func (:obj:`Callable`): The function for re-rendering.
        component (:obj:`ConditionalComponent`): The component associated with the frame.
    """

    def __init__(
        self,
        parent: tk.Canvas,
        controller,
        re_render_func,
        component,
    ):
        super().__init__(
            parent,
            controller,
            re_render_func,
            component,
        )
        assert isinstance(component, ConditionalComponent)
        self.__result = ChainFrame(
            parent, controller, re_render_func, component.get_result()
        )
        self.__condition = ChainFrame(
            parent, controller, re_render_func, component.get_condition()
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
        self.add_type_submenu()
        self.add_delete_button()
        button.bind("<Button-1>", self.show_menu)

    def render(self, x, y):
        """
        Renders the frame at the specified coordinates.

        Args:
            x (int): The x-coordinate to render the widget.
            y (int): The y-coordinate to render the widget.

        Returns:
            int: The y-coordinate after rendering.
        """
        y += super().render(x, y)
        x += Constants.PADDING_PX
        conditional_type = self.get_component().get_form().get_name()
        if conditional_type == "if":
            y = self.__result.render(x, y)
            y = self.create_text_and_get_height("IF", x, y)
            y = self.__condition.render(x, y)
            return y
        elif conditional_type == "if then":
            y = self.create_text_and_get_height("IF", x, y)
            y = self.__condition.render(x, y)
            y = self.create_text_and_get_height("THEN", x, y)
            y = self.__result.render(x, y)
            return y
        raise ValueError("Invalid conditional type")

    def create_text_and_get_height(self, text: str, x: int, y: int):
        """
        Renders text at the specified coordinates.

        Args:
            text (str): The text to render.
            x (int): The x-coordinate to render the text on the canvas.
            y (int): The y-coordinate to render the text on the canvas.

        Returns:
            int: The height of the frame on the canvas.
        """
        parent = self.get_parent()
        label = tk.Message(parent, font=("Arial", 10), text=text, width=500)
        parent.create_window(x, y, anchor=tk.NW, window=label)
        parent.update()
        return y + label.winfo_reqheight()
