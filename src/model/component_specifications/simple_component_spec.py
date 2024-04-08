from typing import Dict, List

from src.model.component_attribute import ComponentAttribute
from src.model.component_specifications.component_spec import ComponentSpec
from src.model.simple_form_spec import SimpleFormSpec


class SimpleComponentSpec(ComponentSpec):
    """
    SimpleComponentSpec class represents the specifications for a simple component.

    Args:
        name (str): The name of the simple component.
        forms (:obj:`list` of :obj:`FormSpec`): The types associated with the simple component.
        attributes (:obj:`list` of :obj:`ComponentAttribute`): The attributes of the simple component.
        location (str): The location of the simple component.
        component_type (str): The name of the type of the component.
    """

    def __init__(
        self,
        name: str,
        forms: List,
        attributes: List[ComponentAttribute],
        location: str,
        component_type: str,
    ) -> None:
        super().__init__(name, forms, location, component_type)
        self.__attributes = attributes

    def get_attributes(self) -> List[ComponentAttribute]:
        """Retrieves the attributes of the simple component."""
        return self.__attributes

    def get_attribute(self, attribute_name: str) -> ComponentAttribute:
        """
        Retrieves a specific attribute of the simple component.

        Args:
            attribute_name(str): The name of the attribute to retrieve.

        Returns:
            The attribute with the specified name.

        Raises:
            ValueError: If the specified attribute name doesn't exist.
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
            json (:obj:`dict`): The JSON data representing the simple component specification.
            constructed_component_specs (:obj:`dict`): Component specs that have already been created.
            terminals (:obj:`list` of :obj:`Terminal`): All defined terminal types.

        Note:
            The JSON object must contain the following attributes:
                component_name of type str.
                form_specs of type list of :obj:`SimpleFormSpec` JSON.
                attributes of type list of :obj:`ComponentAttribute` JSON.
                collection_location of str.


        Returns:
            A SimpleComponentSpec object constructed from the JSON data.
        """
        attributes = cls.attributes_from_json(json, terminals)
        type_specs = cls.form_specs_from_json(json)
        type_specs = [
            SimpleFormSpec.from_json(type_spec) for type_spec in json["form_specs"]
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
            json(:obj:`dict`): The JSON data representing the attributes.

        Returns:
            A list of ComponentAttribute objects parsed from the JSON data.
        """
        return [
            ComponentAttribute.from_json(attribute, terminals)
            for attribute in json["attributes"]
        ]

    @staticmethod
    def form_specs_from_json(json) -> List[SimpleFormSpec]:
        """
        Parses JSON data to create SimpleFormSpec objects.

        Args:
            json: The JSON data representing the type specifications.

        Returns:
            List[SimpleTypeSpec]: A list of SimpleTypeSpec objects parsed from the JSON data.
        """
        return [SimpleFormSpec.from_json(type_spec) for type_spec in json["form_specs"]]
