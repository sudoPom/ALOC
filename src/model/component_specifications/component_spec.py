from abc import ABC, abstractmethod
from typing import Dict, List

from src.model.form_spec import FormSpec


class ComponentSpec(ABC):
    """
    Base class of all Component Specification Classes.

    Args:
        name (str): The name of the component specification.
        forms (:obj:`list` of :obj:`FormSpec`): The list of form specifications associated with the component.
        location (str): The location of the component in the contract.
        component_type (str): The name of the type of the component.
    """

    def __init__(
        self,
        name: str,
        forms: List[FormSpec],
        location: str,
        component_type: str,
    ) -> None:
        self.__name = name
        self.__forms = forms
        self.__location = location
        self.__component_type = component_type

    @classmethod
    @abstractmethod
    def from_json(
        cls, json: Dict, constructed_component_specs: Dict, terminals: Dict
    ) -> "ComponentSpec":
        """
        Creates An Instance of this Component Specification from JSON data.

        Args:
            json (:obj:`Dict`): The JSON data representing the Component Specification.
            constructed_component_specs (:obj:`Dict`): All component specifications that have already been constructed.
            terminals (:obj:`Dict`): All the availble terminal types.
        """
        pass

    def get_name(self) -> str:
        """Returns the name of the component specification."""
        return self.__name

    def get_forms(self) -> List[FormSpec]:
        """Returns the list of type specifications associated with the component."""
        return self.__forms

    def get_contract_location(self) -> str:
        """Returns the location of the component in the contract."""
        return self.__location

    def get_component_type(self) -> str:
        """Returns the type of the component."""
        return self.__component_type

    def get_location(self) -> str:
        """Returns the location of the component."""
        return self.__location
