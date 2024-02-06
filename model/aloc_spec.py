import json

from model.component_collection import ComponentCollection
from model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from model.component_specifications.conditional_component_spec import \
    ConditionalComponentSpec
from model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from model.components.chain_component import ChainComponent
from model.components.conditional_component import ConditionalComponent
from model.components.simple_component import SimpleComponent


class ALOCSpec:
    def __init__(self, path) -> None:
        with open(path) as json_file:
            self.__data = json.load(json_file)
        self.__component_to_spec = {
            "chain_components": ChainComponentSpec,
            "simple_components": SimpleComponentSpec,
            "conditional_components": ConditionalComponentSpec,
        }
        self.__component_types = {
            "chain_component": ChainComponent,
            "simple_component": SimpleComponent,
            "conditional_component": ConditionalComponent,
        }
        self.__contract_collections = []
        self.__component_specs = dict()
        self._initialise_spec()

    def _initialise_spec(self):
        for collection in self.__data["contract"]["collections"]:
            self.__contract_collections.append(ComponentCollection(collection))
        for component_type in self.__component_to_spec.keys():
            components = self.__data[component_type]
            component_spec_class = self.__component_to_spec[component_type]
            for component in components:
                component_spec = component_spec_class.from_json(
                    component, self.__component_specs
                )
                self.__component_specs[component["component_name"]] = component_spec

    def get_contract_collections(self):
        return self.__contract_collections

    def get_component_specs(self):
        return self.__component_specs

    def get_component_types(self):
        return self.__component_types
