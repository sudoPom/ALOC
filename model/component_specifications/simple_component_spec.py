from model.component_attribute import ComponentAttribute
from model.component_specifications.component_spec import ComponentSpec
from model.simple_type_spec import SimpleTypeSpec


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

    @classmethod
    def from_json(cls, json, _):
        attributes = cls.attributes_from_json(json)
        type_specs = cls.type_specs_from_json(json)
        type_specs = [
            SimpleTypeSpec.from_json(type_spec) for type_spec in json["type_specs"]
        ]
        return cls(
            json["component_name"],
            type_specs,
            attributes,
            json["collection_location"],
            "simple_component",
        )

    @staticmethod
    def attributes_from_json(json):
        return [
            ComponentAttribute.from_json(attribute) for attribute in json["attributes"]
        ]

    @staticmethod
    def type_specs_from_json(json):
        return [SimpleTypeSpec.from_json(type_spec) for type_spec in json["type_specs"]]
