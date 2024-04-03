from abc import ABC, abstractmethod
from typing import List, Tuple

from src.model.component_specifications.component_spec import ComponentSpec
from src.model.form_spec import FormSpec


class Component(ABC):
    """Parent class of all component classes.

    Attributes:
        component_spec (ComponentSpec): The specification of the component.
        _id (int): The unique identifier of the component.
        _internal_id (int): The unique internal identifier of the component.
        _types (List[FormSpec]): The possible forms for this component.
        _type (FormSpec): The current form of the component.
        _component_type (str): The type of the component.
        _component_location: The location of the component.
    """

    def __init__(self, component_spec: ComponentSpec) -> None:
        """Initializes a BaseComponent object.

        Args:
            component_spec (ComponentSpec): The specification of the component.
        """
        self._id = 0
        self._internal_id = 0
        self._forms = component_spec.get_forms()
        self._form = self._forms[0]
        self._component_type = component_spec.get_component_type()
        self._component_location = component_spec.get_location()

    def set_form(self, component_form: str) -> None:
        """Sets the type of the component.

        Args:
            component_type (str): The new type of the component.
        """
        self._form = self._get_form_spec(component_form)

    def get_form(self) -> FormSpec:
        """Gets the form of the component.

        Returns:
            FormSpec: The type of the component.
        """
        return self._form

    def get_component_type(self) -> str:
        """Gets the component type.

        Returns:
            str: The type of the component.
        """
        return self._component_type

    def get_forms(self) -> List[FormSpec]:
        """Gets the possible types for this component.

        Returns:
            List[FormSpec]: The possible types of the component.
        """
        return self._forms

    def get_textual_id(self) -> str:
        """Gets the textual form of this component's ID.

        Returns:
            str: The textual form of this component's ID.
        """
        return f"[{self._id}]"

    def get_internal_id(self) -> int:
        """Gets the unique internal identifier of the component.

        Returns:
            int: The unique internal identifier of the component.
        """
        return self._internal_id

    def set_internal_id(self, id: int) -> None:
        """Sets the unique internal identifier of the component.

        Args:
            id (int): The new internal identifier of the component.
        """
        self._internal_id = id

    def set_id(self, id: int) -> None:
        """Sets the unique identifier of the component.

        Args:
            id (int): The new identifier of the component.
        """
        self._id = id

    def _get_form_spec(self, component_form: str) -> FormSpec:
        """Gets the type specification for the given component type.

        Args:
            component_type (str): The type of the component.

        Returns:
            FormSpec: The type specification for the component type.

        Raises:
            ValueError: If the component type is invalid.
        """
        for type_spec in self._forms:
            if type_spec.get_name() == component_form:
                return type_spec
        raise ValueError("Invalid type name.")

    def get_location(self):
        """Gets the location of the component."""
        return self._component_location

    @abstractmethod
    def get_display_text(self) -> str:
        """Gets the display text of the component.

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
             Tuple[int, int]: The next values of the next available unique id and internal id.
        """
        pass

    @abstractmethod
    def to_cola(self) -> str:
        """Converts this component to its textual CoLa form.

        Returns:
            str: The CoLa representation of the component.
        """
        pass
