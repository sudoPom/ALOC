from typing import Dict, List

from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.component_specifications.component_spec import ComponentSpec
from src.model.form_spec import FormSpec


class ConditionalComponentSpec(ComponentSpec):
    """
    ConditionalComponentSpec class represents the specifications for a conditional component.

    Args:
        name (str): The name of the component.
        forms (:obj:`list` of :obj:`SimpleFormSpec`): The forms associated with the component.
        location (str): The location of the chain component within the contract.
        component_type (str): The name of the type of the component.
        condition_spec (:obj:`ChainComponentSpec`): The component specification describing the condition of the component.
        result_spec (:obj:`ChainComponentSpec`): The component specification describing the result of the component.
    """

    def __init__(
        self,
        name: str,
        forms: List[FormSpec],
        location: str,
        component_type: str,
        condition_spec: ChainComponentSpec,
        result_spec: ChainComponentSpec,
    ) -> None:
        super().__init__(name, forms, location, component_type)
        self.__condition_spec = condition_spec
        self.__result_spec = result_spec

    def get_result_spec(self) -> ChainComponentSpec:
        """
        Returns the specification of the result Component.

        Returns:
            :obj:`ChainComponentSpec`: The specification of the result component.
        """
        return self.__result_spec

    def get_condition_spec(self) -> ChainComponentSpec:
        """
        Returns the specification of the condition Component.

        Returns:
            :obj:`ChainComponentSpec`: The specification of the condition component.
        """
        return self.__condition_spec

    @classmethod
    def from_json(
        cls, json: Dict, constructed_component_specs, terminals
    ) -> "ConditionalComponentSpec":
        """
        Constructs a ConditionalComponentSpec object from JSON data.

        Args:
            json (:obj:`dict`): The JSON data representing the conditional component specification.
            constructed_component_specs (:obj:`dict`): Component specs that have already been created.
            terminals (:obj:`list` of :obj:`Terminal`): All defined terminal types.
        Note:
            The JSON object must contain the following attributes:
                component_name of type str.
                form_specs of type list of :obj:`FormSpec` JSON.
                result of type :obj:`ChainComponentSpec` JSON.
                condition of type :obj:`ChainComponentSpec` JSON.
                collection_location of type str.

        Returns:
            A ConditionalComponentSpec object constructed from the JSON data.
        """
        type_specs = [FormSpec.from_json(type_spec) for type_spec in json["form_specs"]]
        result_spec = constructed_component_specs[json["result"]]
        condition_spec = constructed_component_specs[json["condition"]]
        return cls(
            json["component_name"],
            type_specs,
            json["collection_location"],
            "conditional_component",
            condition_spec,
            result_spec,
        )
