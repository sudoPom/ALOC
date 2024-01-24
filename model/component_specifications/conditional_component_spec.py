from model.component_specifications.component_spec import ComponentSpec


class ConditionalComponentSpec(ComponentSpec):
    def __init__(
        self,
        name,
        types,
        location,
        component_type,
        condition_spec,
        result_spec,
    ):
        super().__init__(name, types, location, component_type)
        self.__condition_spec = condition_spec
        self.__result_spec = result_spec

    def get_result_spec(self):
        return self.__result_spec

    def get_condition_spec(self):
        return self.__condition_spec
