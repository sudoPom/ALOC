from view.constants import Constants
from view.frames import (base_frame, chain_frame, conditional_frame,
                         contract_frame)


class Renderer:
    def __init__(self, frame, controller, re_render_func):
        self.__frame = frame.get_canvas()
        self.__controller = controller
        self.__re_render_func = re_render_func

    def render(self, x, y, contract):
        self.__frame.delete("all")
        y += contract_frame.ContractFrame(
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

    def render_component(self, x, y, component):
        match component.get_component_type():
            case "simple_component":
                y = base_frame.BaseFrame(
                    self.__frame,
                    self.__controller,
                    self.__re_render_func,
                    component,
                    {"updatable", "deletable", "multi-typed"},
                ).render(x, y)
            case "chain_component":
                y = chain_frame.ChainFrame(
                    self.__frame,
                    self.__controller,
                    self.__re_render_func,
                    component,
                ).render(x, y)
            case "conditional_component":
                y = conditional_frame.ConditionalFrame(
                    self.__frame, self.__controller, self.__re_render_func, component
                ).render(x, y)
        return y
