from tkinter import Canvas
from typing import Callable

from controller.controller import Controller
from model.component_collection import ComponentCollection
from model.components.component import Component
from model.components.contract import Contract
from view.constants import Constants
from view.frames.base_frame import BaseFrame
from view.frames.chain_frame import ChainFrame
from view.frames.conditional_frame import ConditionalFrame
from view.frames.contract_frame import ContractFrame
from view.scroll_canvas import ScrollCanvas


class Renderer:
    """
    Renderer class responsible for rendering components on the canvas.

    Methods:
    - __init__(frame, controller, re_render_func): Initializes a Renderer object.
    - render(x, y, contract): Renders the components of the contract.
    - render_component(x, y, component): Renders a specific component.
    """

    def __init__(
        self,
        frame: ScrollCanvas,
        controller: Controller,
        re_render_func: Callable,
    ) -> None:
        """
        Initializes a Renderer object.

        Args:
        - frame (Canvas): The frame to render components on.
        - controller (ContractController): The controller for managing component actions.
        - re_render_func (callable): The function to call for re-rendering.
        """
        self.__frame: Canvas = frame.get_canvas()
        self.__controller: Controller = controller
        self.__re_render_func: Callable = re_render_func

    def render(self, x: int, y: int, contract: Contract) -> None:
        """
        Renders the components of the contract.

        Args:
        - x (int): The starting x-coordinate for rendering.
        - y (int): The starting y-coordinate for rendering.
        - contract (Contract): The contract to render.
        """
        self.__frame.delete("all")
        y += ContractFrame(
            self.__frame,
            self.__controller,
            self.__re_render_func,
            self.__controller.get_contract_component_names(),
        ).render(x, y)
        x += Constants.INDENT_SIZE_PX
        for component_collection in contract.get_component_collections():
            components = component_collection.get_components()
            for component in components:
                y = self.render_component(x, y, component)

    def render_component(self, x: int, y: int, component: Component) -> int:
        """
        Renders a specific component.

        Args:
        - x (int): The x-coordinate for rendering.
        - y (int): The y-coordinate for rendering.
        - component (Component): The component to render.

        Returns:
        - int: The updated y-coordinate after rendering the component.
        """
        match component.get_component_type():
            case "simple_component":
                y = BaseFrame(
                    self.__frame,
                    self.__controller,
                    self.__re_render_func,
                    component,
                    {"updatable", "deletable", "multi-typed"},
                ).render(x, y)
            case "chain_component":
                y = ChainFrame(
                    self.__frame,
                    self.__controller,
                    self.__re_render_func,
                    component,
                ).render(x, y)
            case "conditional_component":
                y = ConditionalFrame(
                    self.__frame, self.__controller, self.__re_render_func, component
                ).render(x, y)
        return y
