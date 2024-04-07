"""
Component
=========
Module representing the parent class of all Components.
"""
from abc import ABC, abstractmethod
from typing import List, Tuple

from src.model.component_specifications.component_spec import ComponentSpec
from src.model.form_spec import FormSpec


class Component(ABC):
    """Parent class of all component classes.

    Args:
        component_spec (ComponentSpec): The specification of the component.
    """

    def __init__(self, component_spec: ComponentSpec) -> None:
        self._id = 0
        self._internal_id = 0
        self._forms = component_spec.get_forms()
        self._form = self._forms[0]
        self._component_type = component_spec.get_component_type()
        self._component_location = component_spec.get_location()

    @abstractmethod
    def get_display_text(self) -> str:
        """
        Gets the display text of the component.

        Returns:
            str: The display text of the component.
        """
        pass

    @abstractmethod
    def reset_id(self, id: int, internal_id: int) -> Tuple[int, int]:
        """Resets the id (internal and non-internal) of the component.

        Args:
            id (int): The new identifier of the component.
            internal_id (int): The new internal identifier of the component.

        Returns:
             :obj:`tuple` of :obj:`[int, int]`: The next values of the next available unique id and internal id.
        """
        pass

    @abstractmethod
    def to_cola(self) -> str:
        """
        Converts this component to its textual CoLa form.

        Returns:
            str: The CoLa representation of the component.
        """
        pass

    def get_textual_id(self) -> str:
        """Gets the textual form of this component's ID.

        Returns:
            str: The textual form of this component's ID in the form [ID].
        """
        return f"[{self._id}]"

    def set_form(self, component_form: str) -> None:
        """
        Gets the display text of the component.

        Returns:
            str: The display text of the component.
        """
        self._form = self._get_form_spec(component_form)

    def get_form(self) -> FormSpec:
        """
        Gets the current form of the component.

        Returns:
            :obj:`FormSpec`: The current form of the component.
        """
        return self._form

    def get_component_type(self) -> str:
        """
        Gets the type of the component.

        Returns:
            str: The type of the component.
        """
        return self._component_type

    def get_forms(self) -> List[FormSpec]:
        """
        Gets all the possible forms of the component.

        Returns:
            :obj:`List[FormSpec]`: All the possible forms of the component.
        """
        return self._forms

    def get_internal_id(self) -> int:
        """
        Gets the internal id of the component.

        Returns:
            int: The internal id of the component.
        """
        return self._internal_id

    def set_internal_id(self, id: int) -> None:
        """
        Sets the internal_id of the component.

        Args:
            id (int): The value to set the internal id to.
        """
        self._internal_id = id

    def set_id(self, id: int) -> None:
        """
        Sets the id of the component.

        Args:
            id (int): The value to set the id to.
        """
        self._id = id

    def _get_form_spec(self, component_form: str) -> FormSpec:
        for type_spec in self._forms:
            if type_spec.get_name() == component_form:
                return type_spec
        raise ValueError("Invalid type name.")

    def get_location(self):
        """
        Gets the location of the component in the contract.

        Returns:
            str: The name of the location of the component.
        """
        return self._component_location
