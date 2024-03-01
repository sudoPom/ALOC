import tkinter as tk
from typing import Callable, List

from src.controller.controller import Controller


class ContractFrame(tk.Frame):
    """
    ContractFrame class represents the frame for displaying contract components in the GUI.

    Attributes:
    - __parent (tk.Frame): The parent frame.
    - __controller: The controller managing component actions.
    - __re_render_func: The function for re-rendering.
    - __menu (tk.Menu): The menu for adding components.
    - __components (list): The list of component names.

    Methods:
    - __init__(parent, controller, re_render_func, components, **kwargs): Initializes a ContractFrame object.
    - create_widgets(): Creates the widgets for the frame.
    - show_menu(event): Displays the context menu.
    - add_menu_command(component_name): Adds a menu command for adding a new component.
    - add_new_component(component_name): Adds a new component.
    - render(x, y): Renders the frame at the specified coordinates.
    """

    def __init__(
        self,
        parent: tk.Canvas,
        controller: Controller,
        re_render_func: Callable,
        components: List[str],
        **kwargs,
    ):
        """
        Initializes a ContractFrame object.

        Args:
        - parent (tk.Frame): The parent frame.
        - controller (Callable): The controller managing component actions.
        - re_render_func (Callable): The function for re-rendering.
        - components (list): The list of component names.
        - **kwargs: Additional keyword arguments.
        """
        super().__init__(parent, **kwargs)
        self.__parent = parent
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.__menu: tk.Menu = tk.Menu(self, tearoff=0)
        self.__components: List[str] = list(components)
        self.create_widgets()

    def create_widgets(self) -> None:
        """Creates the widgets for the frame."""
        button = tk.Button(self, text="Contract", bg="red")
        button.pack()
        self.__menu = tk.Menu(self, tearoff=0)
        for component in self.__components:
            self.add_menu_command(component)
        button.bind("<Button-1>", self.show_menu)

    def show_menu(self, event: tk.Event) -> None:
        """Displays the context menu."""
        self.__menu.tk_popup(event.x_root, event.y_root)

    def add_menu_command(self, component_name: str) -> None:
        """
        Adds a menu command for adding a new component.

        Args:
        - component_name (str): The name of the component.
        """
        self.__menu.add_command(
            label=f"Add {component_name.capitalize().replace('_', ' ')}",
            command=lambda: self.add_new_component(component_name),
        )

    def add_new_component(self, component_name: str) -> None:
        """
        Adds a new component.

        Args:
        - component_name (str): The name of the component.
        """
        self.__controller.add_new_component(component_name)
        self.__re_render_func()

    def render(self, x: int, y: int) -> int:
        """
        Renders the frame at the specified coordinates.

        Args:
        - x (int): The x-coordinate.
        - y (int): The y-coordinate.

        Returns:
        - int: The y-coordinate after rendering.
        """
        self.__parent.create_window(x, y, anchor=tk.NW, window=self)
        self.__parent.update()
        y += self.winfo_reqheight()
        return y
