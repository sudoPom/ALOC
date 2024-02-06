import json
from typing import Dict, List

from model.component_collection import ComponentCollection
from model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from model.component_specifications.component_spec import ComponentSpec
from model.component_specifications.conditional_component_spec import \
    ConditionalComponentSpec
from model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from model.components.chain_component import ChainComponent
from model.components.component import Component
from model.components.conditional_component import ConditionalComponent
from model.components.simple_component import SimpleComponent


class ALOCSpec:
    """
    ALOCSpec class represents the specifications for the contract defined in an ALOC (Application Level Object Contract) file.

    Methods:
    - __init__(path): Initializes an ALOCSpec object from the specified ALOC file path.
    - get_contract_collections(): Retrieves the component collections defined in the ALOC file.
    - get_component_specs(): Retrieves the component specifications defined in the ALOC file.
    - get_component_types(): Retrieves the types of components defined in the ALOC file.
    """

    def __init__(self, path: str) -> None:
        """
        Initializes an ALOCSpec object from the specified ALOC file path.

        Args:
        - path (str): The path to the ALOC file.
        """
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
        """
        Initializes the ALOCSpec object by parsing the data from the ALOC file and constructing component collections and component specifications.
        """
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

    def get_contract_collections(self) -> List[ComponentCollection]:
        """
        Retrieves the component collections defined in the ALOC file.

        Returns:
        - List[ComponentCollection]: A list of ComponentCollection objects representing the component collections.
        """
        return self.__contract_collections

    def get_component_specs(self) -> Dict[str, ComponentSpec]:
        """
        Retrieves the component specifications defined in the ALOC file.

        Returns:
        - Dict[str, ComponentSpec]: A dictionary mapping component names to their corresponding ComponentSpec objects.
        """
        return self.__component_specs

    def get_component_types(self) -> Dict[str, Component]:
        """
        Retrieves the types of components defined in the ALOC file.

        Returns:
        - Dict[str, Component]: A dictionary mapping component names to their corresponding Component types.
        """
        return self.__component_types
