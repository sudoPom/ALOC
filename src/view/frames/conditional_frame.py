import tkinter as tk

from src.model.components.conditional_component import ConditionalComponent
from src.view.constants import Constants
from src.view.frames.base_frame import BaseFrame
from src.view.frames.chain_frame import ChainFrame


class ConditionalFrame(BaseFrame):
    """
    ConditionalFrame class represents the frame for conditional components in the GUI.

    Attributes:
    - __result (ChainFrame): The frame representing the result of the conditional.
    - __condition (ChainFrame): The frame representing the condition of the conditional.

    Methods:
    - __init__(parent, controller, re_render_func, conditional, **kwargs): Initializes a ConditionalFrame object.
    - render(x, y): Renders the frame at the specified coordinates.
    - create_text_and_get_height(text, x, y): Creates a text label and returns its height.
    """

    def __init__(
        self,
        parent: tk.Canvas,
        controller,
        re_render_func,
        conditional,
        **kwargs,
    ):
        """
        Initializes a ConditionalFrame object.

        Args:
        - parent (tk.Canvas): The parent canvas.
        - controller: The controller managing component actions.
        - re_render_func: The function for re-rendering.
        - conditional: The conditional component associated with the frame.
        - **kwargs: Additional keyword arguments.
        """
        super().__init__(
            parent,
            controller,
            re_render_func,
            conditional,
            **kwargs,
        )
        component = self.get_component()
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
            text=self.get_component().get_type().get_display_text(),
            bg=self.get_component().get_type().get_colour(),
        )
        button.grid(row=0, column=0, sticky=tk.W)
        self.add_type_submenu()
        self.add_delete_button()
        button.bind("<Button-1>", self.show_menu)

    def render(self, x, y):
        """
        Renders the frame at the specified coordinates.

        Args:
        - x: The x-coordinate.
        - y: The y-coordinate.

        Returns:
        - int: The y-coordinate after rendering.
        """
        y += super().render(x, y)
        x += Constants.PADDING_PX
        conditional_type = self.get_component().get_type().get_name()
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

    def create_text_and_get_height(self, text, x, y):
        """
        Creates a text label and returns its height.

        Args:
        - text (str): The text to display.
        - x: The x-coordinate.
        - y: The y-coordinate.

        Returns:
        - int: The height of the text label.
        """
        parent = self.get_parent()
        label = tk.Message(parent, font=("Arial", 10), text=text, width=500)
        parent.create_window(x, y, anchor=tk.NW, window=label)
        parent.update()
        return y + label.winfo_reqheight()
