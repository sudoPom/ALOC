import json
from typing import Dict, List, Type

from src.model.component_collection import ComponentCollection
from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.component_specifications.component_spec import ComponentSpec
from src.model.component_specifications.conditional_component_spec import \
    ConditionalComponentSpec
from src.model.component_specifications.else_conditional_component_spec import \
    ElseConditionalComponentSpec
from src.model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from src.model.components.chain_component import ChainComponent
from src.model.components.component import Component
from src.model.components.conditional_component import ConditionalComponent
from src.model.components.else_conditional_component import \
    ElseConditionalComponent
from src.model.components.simple_component import SimpleComponent
from src.model.terminal_types.hybrid_terminal import HybridTerminal
from src.model.terminal_types.multi_choice_terminal import MultiChoiceTerminal
from src.model.terminal_types.terminal import TerminalTypeNames
from src.model.terminal_types.text_terminal import TextTerminal
from src.parser.base_parser import BaseParser


class ALOCSpec:
    """
    ALOCSpec class contains details on all the specifications defined in an ALOC file.

    Args:
        path (str): The path of the ALOC Spec to read.
    """

    def __init__(self, path: str) -> None:
        with open(path) as json_file:
            self.__data = json.load(json_file)
        self.__component_to_spec = {
            "chain_components": ChainComponentSpec,
            "simple_components": SimpleComponentSpec,
            "conditional_components": ConditionalComponentSpec,
            "else_conditional_components": ElseConditionalComponentSpec,
        }
        self.__component_types = {
            "chain_component": ChainComponent,
            "simple_component": SimpleComponent,
            "conditional_component": ConditionalComponent,
            "else_conditional_component": ElseConditionalComponent,
        }
        self.__terminal_types = [
            terminal_type_name.value for terminal_type_name in TerminalTypeNames
        ]
        self.__terminal_types_to_objects = dict()
        self.__contract_collections = []
        with open(self.__data["contract"]["grammar_path"]) as grammar_file:
            self.__grammar = grammar_file.read()
        self.__component_specs = dict()
        self._initialise_spec()

    def _initialise_spec(self):
        self._initialise_terminals()
        for collection in self.__data["contract"]["collections"]:
            self.__contract_collections.append(ComponentCollection(collection))
        for component_type in self.__component_to_spec.keys():
            components = self.__data[component_type]
            component_spec_class = self.__component_to_spec[component_type]
            for component in components:
                component_spec = component_spec_class.from_json(
                    component, self.__component_specs, self.__terminal_types_to_objects
                )
                self.__component_specs[component["component_name"]] = component_spec

    def _initialise_terminals(self):
        for terminal_type in self.__terminal_types:
            terminals = self.__data["terminal_types"][terminal_type]
            for terminal in terminals:
                self.__terminal_types_to_objects[
                    terminal["name"]
                ] = self._initialise_terminal(terminal, terminal_type)

    def _initialise_terminal(self, terminal, terminal_type: str):
        match (terminal_type):
            case TerminalTypeNames.TEXT.value:
                parser = BaseParser(terminal["parse_root"], self.__grammar)
                return TextTerminal(
                    terminal["name"],
                    terminal["default"],
                    parser,
                    terminal["explanation"],
                )
            case TerminalTypeNames.MULTI_CHOICE.value:
                if "allow_empty" in terminal and terminal["allow_empty"]:
                    allow_empty = True
                else:
                    allow_empty = False
                return MultiChoiceTerminal(
                    terminal["name"],
                    terminal["default"],
                    terminal["choices"],
                    allow_empty,
                )
            case TerminalTypeNames.HYBRID.value:
                parser = BaseParser(terminal["parse_root"], self.__grammar)
                return HybridTerminal(
                    terminal["name"],
                    terminal["default_option"],
                    terminal["default_text"],
                    parser,
                    terminal["explanation"],
                    terminal["choices"],
                )
            case _:
                raise ValueError(
                    f"Unsupported terminal type specified in ALOC sepc: {terminal_type}"
                )

    def get_contract_collections(self) -> List[ComponentCollection]:
        """
        Retrieves the component collections defined in the ALOC file.

        Returns:
            :obj:`List[ComponentCollection]`: A list of ComponentCollection objects representing the component collections.
        """
        return self.__contract_collections

    def get_component_specs(self) -> Dict[str, ComponentSpec]:
        """
        Retrieves the component specifications defined in the ALOC file.

        Returns:
            :obj:`Dict[str, ComponentSpec]`: A dictionary mapping component names to their corresponding ComponentSpec objects.
        """
        return self.__component_specs

    def get_component_types(self) -> Dict[str, Type[Component]]:
        """
        Retrieves the types of components defined in the ALOC file.

        Returns:
            :obj:`Dict[str, Component]`: A dictionary mapping component names to their corresponding Component types.
        """
        return self.__component_types
