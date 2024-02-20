from typing import Dict, List

from model.component_attribute import ComponentAttribute
from model.component_specifications.component_spec import ComponentSpec
from model.simple_type_spec import SimpleTypeSpec


class SimpleComponentSpec(ComponentSpec):
    """
    SimpleComponentSpec class represents the specifications for a simple component.

    This class inherits from ComponentSpec.

    Methods:
    - __init__(name, types, attributes, location, component_type): Initializes a SimpleComponentSpec object.
    - get_attributes(): Retrieves the attributes of the simple component.
    - get_attribute(attribute_name): Retrieves a specific attribute of the simple component.
    - from_json(json, _): Constructs a SimpleComponentSpec object from JSON data.
    - attributes_from_json(json): Parses JSON data to create ComponentAttribute objects.
    - type_specs_from_json(json): Parses JSON data to create SimpleTypeSpec objects.

    Attributes:
    - Inherits all attributes from the ComponentSpec class.
    """

    def __init__(
        self,
        name: str,
        types: List[SimpleTypeSpec],
        attributes: List[ComponentAttribute],
        location: str,
        component_type: str,
    ) -> None:
        """
        Initializes a SimpleComponentSpec object.

        Args:
        - name: The name of the simple component.
        - types: The types associated with the simple component.
        - attributes: The attributes of the simple component.
        - location: The location of the simple component.
        - component_type: The type of the component.
        """
        super().__init__(name, types, location, component_type)
        self.__attributes = attributes

    def get_attributes(self) -> List[ComponentAttribute]:
        """Retrieves the attributes of the simple component."""
        return self.__attributes

    def get_attribute(self, attribute_name: str) -> ComponentAttribute:
        """
        Retrieves a specific attribute of the simple component.

        Args:
        - attribute_name: The name of the attribute to retrieve.

        Returns:
        - ComponentAttribute: The attribute with the specified name.

        Raises:
        - ValueError: If the specified attribute name is invalid.
        """
        for attribute in self.__attributes:
            if attribute.get_name() == attribute_name:
                return attribute
        raise ValueError(f"Invalid Attribute: {attribute_name}")

    @classmethod
    def from_json(
        cls, json: Dict, constructed_component_specs, terminals
    ) -> "SimpleComponentSpec":
        """
        Constructs a SimpleComponentSpec object from JSON data.

        Args:
        - json: The JSON data representing the simple component.
        - _: Placeholder argument.

        Returns:
        - SimpleComponentSpec: A SimpleComponentSpec object constructed from the JSON data.
        """
        attributes = cls.attributes_from_json(json, terminals)
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
    def attributes_from_json(json: Dict, terminals) -> List[ComponentAttribute]:
        """
        Parses JSON data to create ComponentAttribute objects.

        Args:
        - json: The JSON data representing the attributes.

        Returns:
        - List[ComponentAttribute]: A list of ComponentAttribute objects parsed from the JSON data.
        """
        return [
            ComponentAttribute.from_json(attribute, terminals)
            for attribute in json["attributes"]
        ]

    @staticmethod
    def type_specs_from_json(json) -> List[SimpleTypeSpec]:
        """
        Parses JSON data to create SimpleTypeSpec objects.

        Args:
        - json: The JSON data representing the type specifications.

        Returns:
        - List[SimpleTypeSpec]: A list of SimpleTypeSpec objects parsed from the JSON data.
        """
        return [SimpleTypeSpec.from_json(type_spec) for type_spec in json["type_specs"]]
