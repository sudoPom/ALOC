from model.component_specifications.component_spec import ComponentSpec


class SimpleComponentSpec(ComponentSpec):
    def __init__(self, name, types, attributes, location, component_type):
        super().__init__(name, types, location, component_type)
        self.__attributes = attributes

    def get_attributes(self):
        return self.__attributes

    def get_attribute(self, attribute_name):
        for attribute in self.__attributes:
            if attribute.get_name() == attribute_name:
                return attribute
        raise ValueError(f"Invalid Attribute: {attribute_name}")
