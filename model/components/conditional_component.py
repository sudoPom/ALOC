from model.components.chain_component import ChainComponent
from model.components.component import Component


class ConditionalComponent(Component):
    def __init__(self, conditional_component_spec):
        super().__init__(conditional_component_spec)

        self.__condition_component = ChainComponent(
            conditional_component_spec.get_condition_spec()
        )
        self.__result_component = ChainComponent(
            conditional_component_spec.get_result_spec()
        )

    def get_result(self):
        return self.__result_component

    def get_condition(self):
        return self.__condition_component

    def get_display_text(self):
        return None

    def reset_id(self, id):
        current_type = self.get_type().get_name()
        if current_type == "if":
            id = self.__result_component.reset_id(id)
            return self.__condition_component.reset_id(id)
        elif current_type == "if then":
            id = self.__condition_component.reset_id(id)
            return self.__result_component.reset_id(id)
