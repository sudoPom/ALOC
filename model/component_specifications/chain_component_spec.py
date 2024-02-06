from typing import List, Self

from model.component_attribute import ComponentAttribute
from model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from model.simple_type_spec import SimpleTypeSpec
from model.type_spec import TypeSpec


class ChainComponentSpec(SimpleComponentSpec):
    """
    ChainComponentSpec class represents the specifications for a chain component.

    This class inherits from SimpleComponentSpec.

    Methods:
    - __init__(name, types, attributes, location, component_type): Initializes a ChainComponentSpec object.
    - from_json(json, _): Constructs a ChainComponentSpec object from JSON data.

    Attributes:
    - Inherits all attributes from the SimpleComponentSpec class.
    """

    def __init__(
        self,
        name: str,
        types: List[SimpleTypeSpec],
        attributes: List[ComponentAttribute],
        location: str,
        component_type: str,
    ):
        """
        Initializes a ChainComponentSpec object.

        Args:
        - name: The name of the chain component.
        - types: The types associated with the chain component.
        - attributes: The attributes of the chain component.
        - location: The location of the chain component.
        - component_type: The type of the component.
        """
        super().__init__(name, types, attributes, location, component_type)

    @classmethod
    def from_json(cls, json: Dict, constructed_component_specs) -> "ChainComponentSpec":
        """
        Constructs a ChainComponentSpec object from JSON data.

        Args:
        - json: The JSON data representing the chain component.
        - _: Placeholder argument.

        Returns:
        - ChainComponentSpec: A ChainComponentSpec object constructed from the JSON data.
        """
        attributes = cls.attributes_from_json(json)
        type_specs = cls.type_specs_from_json(json)
        return cls(
            json["component_name"],
            type_specs,
            attributes,
            json["collection_location"],
            "chain_component",
        )
