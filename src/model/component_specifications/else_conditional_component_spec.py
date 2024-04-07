from typing import Dict, List

from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.component_specifications.conditional_component_spec import \
    ConditionalComponentSpec
from src.model.form_spec import FormSpec


class ElseConditionalComponentSpec(ConditionalComponentSpec):
    def __init__(
        self,
        name: str,
        forms: List[FormSpec],
        location: str,
        component_type: str,
        condition_spec: ChainComponentSpec,
        result_spec: ChainComponentSpec,
    ) -> None:
        super().__init__(
            name, forms, location, component_type, condition_spec, result_spec
        )
        self.__else_spec = result_spec

    def get_else_spec(self):
        return self.__else_spec

    @classmethod
    def from_json(
        cls, json: Dict, constructed_component_specs, terminals
    ) -> "ElseConditionalComponentSpec":
        """
        Constructs a ElseConditionalComponentSpec object from JSON data.

        Args:
            json (:obj:`dict`): The JSON data representing the else conditional component specification.
            constructed_component_specs (:obj:`dict`): Component specs that have already been created.
            terminals (:obj:`list` of :obj:`Terminal`): All defined terminal types.

        Returns:
            A ElseConditionalComponentSpec object constructed from the JSON data.
        """
        type_specs = [FormSpec.from_json(type_spec) for type_spec in json["form_specs"]]
        result_spec = constructed_component_specs[json["result"]]
        condition_spec = constructed_component_specs[json["condition"]]
        return cls(
            json["component_name"],
            type_specs,
            json["collection_location"],
            "else_conditional_component",
            condition_spec,
            result_spec,
        )
