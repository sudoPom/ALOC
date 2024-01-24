from model.components.chain_component import ChainComponent
from model.components.component import Component


class ConditionalComponent(Component):
    def __init__(self, component_id, conditional_component_spec):
        super().__init__(component_id, conditional_component_spec)

        self.__condition_component = ChainComponent(
            component_id + 1, conditional_component_spec.get_condition_spec()
        )
        self.__result_component = ChainComponent(
            component_id + 2, conditional_component_spec.get_result_spec()
        )

    def get_result(self):
        return self.__result_component

    def get_condition(self):
        return self.__condition_component

    def get_display_text(self):
        return None
