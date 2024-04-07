from tkinter import Canvas
from typing import Callable

from src.controller.controller import Controller
from src.model.components.chain_component import ChainComponent
from src.model.components.component import Component
from src.model.components.conditional_component import ConditionalComponent
from src.model.components.contract import Contract
from src.model.components.else_conditional_component import \
    ElseConditionalComponent
from src.model.components.simple_component import SimpleComponent
from src.view.constants import Constants
from src.view.frames.chain_frame import ChainFrame
from src.view.frames.conditional_frame import ConditionalFrame
from src.view.frames.contract_frame import ContractFrame
from src.view.frames.else_conditional_frame import ElseConditionalFrame
from src.view.frames.simple_frame import SimpleFrame
from src.view.scroll_canvas import ScrollCanvas

COMPONENTS_TO_FRAMES = {
    ChainComponent: ChainFrame,
    SimpleComponent: SimpleFrame,
    ConditionalComponent: ConditionalFrame,
    ElseConditionalComponent: ElseConditionalFrame,
}


class Renderer:
    """
    Renderer class responsible for rendering components on the canvas.

    Methods:
        __init__(frame, controller, re_render_func): Initializes a Renderer object.
        render(x, y, contract): Renders the components of the contract.
        render_component(x, y, component): Renders a specific component.
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
            frame (Canvas): The frame to render components on.
            controller (ContractController): The controller for managing component actions.
            re_render_func (callable): The function to call for re-rendering.
        """
        self.__frame: Canvas = frame.get_canvas()
        self.__controller: Controller = controller
        self.__re_render_func: Callable = re_render_func

    def render(self, x: int, y: int, contract: Contract) -> None:
        """
        Renders the components of the contract.

        Args:
            x (int): The starting x-coordinate for rendering.
            y (int): The starting y-coordinate for rendering.
            contract (Contract): The contract to render.
        """
        self.__frame.delete("all")
        y = ContractFrame(
            self.__frame,
            self.__controller,
            self.__re_render_func,
            self.__controller.get_contract_component_names(),
        ).render(x, y)
        x += Constants.INDENT_SIZE_PX
        for component_collection in contract.get_component_collections():
            components = component_collection.get_components()
            for component in components:
                print(component)
                y = self.render_component(x, y, component)

    def render_component(self, x: int, y: int, component: Component) -> int:
        """
        Renders a specific component.

        Args:
            x (int): The x-coordinate for rendering.
            y (int): The y-coordinate for rendering.
            component (Component): The component to render.

        Returns:
            int: The updated y-coordinate after rendering the component.
        """
        component_type = type(component)
        assert (
            component_type in COMPONENTS_TO_FRAMES
        ), f"{component_type} either doesn't exists or doesnt have an associated frame."
        frame_type = COMPONENTS_TO_FRAMES[component_type]
        return frame_type(
            self.__frame, self.__controller, self.__re_render_func, component
        ).render(x, y)
