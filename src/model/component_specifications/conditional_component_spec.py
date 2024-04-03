from typing import Dict, List

from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.component_specifications.component_spec import ComponentSpec
from src.model.form_spec import FormSpec


class ConditionalComponentSpec(ComponentSpec):
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
        return self.__result_spec

    def get_condition_spec(self) -> ChainComponentSpec:
        return self.__condition_spec

    @classmethod
    def from_json(
        cls, json: Dict, constructed_component_specs, terminals
    ) -> "ConditionalComponentSpec":
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
