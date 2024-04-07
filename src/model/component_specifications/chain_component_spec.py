from typing import Dict, List

from src.model.component_attribute import ComponentAttribute
from src.model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from src.model.simple_form_spec import SimpleFormSpec


class ChainComponentSpec(SimpleComponentSpec):
    """
    ChainComponentSpec class represents the specifications for a chain component.

    Args:
        name (str): The name of the component.
        forms (:obj:`list` of :obj:`SimpleFormSpec`): The forms associated with the chain component.
        attributes (:obj:`list` of :obj:`ComponentAttribute`): The attributes of the chain component.
        location (str): The location of the chain component within the contract.
        linking_attribute: (str) The name of the attribute that links together chain components.
        component_type: (str) The name of the type of the component.
    """

    def __init__(
        self,
        name: str,
        forms: List,
        attributes: List[ComponentAttribute],
        location: str,
        linking_attribute: str,
        component_type: str,
    ):
        super().__init__(name, forms, attributes, location, component_type)
        self.__linking_attribute = linking_attribute

    def create_blank(self):
        attributes = [attribute.create_blank() for attribute in self.get_attributes()]
        forms = self.get_forms()
        assert isinstance(forms, List)
        assert all(isinstance(_type, SimpleFormSpec) for _type in forms)
        new_spec = ChainComponentSpec(
            self.get_name(),
            forms,
            attributes,
            self.get_location(),
            self.__linking_attribute,
            "chain_component",
        )
        return new_spec

    def get_linking_attribute(self):
        """
        Gets the linking attribute of the component spec.
        """
        return self.__linking_attribute

    @classmethod
    def from_json(
        cls, json: Dict, constructed_component_specs, terminals
    ) -> "ChainComponentSpec":
        """
        Constructs a ChainComponentSpec object from JSON data.

        Args:
            json (:obj:`dict`): The JSON data representing the chain component specification.
            constructed_component_specs (:obj:`dict`): Component specs that have already been created.
            terminals (:obj:`list` of :obj:`Terminal`): All defined terminal types.

        Returns:
            A ChainComponentSpec object constructed from the JSON data.
        """
        attributes = cls.attributes_from_json(json, terminals)
        form_specs = cls.form_specs_from_json(json)
        return cls(
            json["component_name"],
            form_specs,
            attributes,
            json["collection_location"],
            json["linking_attribute"],
            "chain_component",
        )
