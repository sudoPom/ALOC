from typing import List

from model.component_specifications.component_spec import ComponentSpec
from model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from model.type_spec import TypeSpec


class ConditionalComponentSpec(ComponentSpec):
    def __init__(
        self,
        name: str,
        types: List[TypeSpec],
        location: str,
        component_type: str,
        condition_spec: SimpleComponentSpec,
        result_spec: SimpleComponentSpec,
    ):
        super().__init__(name, types, location, component_type)
        self.__condition_spec = condition_spec
        self.__result_spec = result_spec

    def get_result_spec(self):
        return self.__result_spec

    def get_condition_spec(self):
        return self.__condition_spec

    @classmethod
    def from_json(cls, json, constructed_component_specs) -> "ConditionalComponentSpec":
        type_specs = [TypeSpec.from_json(type_spec) for type_spec in json["type_specs"]]
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
