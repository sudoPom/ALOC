from abc import ABC, abstractmethod
from typing import List, TypeVar

from model.component_specifications.component_spec import ComponentSpec
from model.type_spec import TypeSpec

T = TypeVar("T", bound=TypeSpec)


class Component(ABC):
    """
    Parent class of all component classes.

    Args:
    - component_spec (ComponentSpec): The specification of the component.

    Methods:
    - update(**kwargs): Update the attributes of the component with the provided keyword arguments.
    - set_type(type): Set the type of the component.
    - get_type(): Get the type of the component.
    - get_id(): Get the unique identifier of the component.
    - extract_key(kwargs, key, default): Extract the value of a key from kwargs, with a default value if the key is not present.
    - throw_if_no_keys_found(kwargs, expected_keys): Throw an error if none of the expected keys are found in kwargs.
    """

    def __init__(self, component_spec: ComponentSpec) -> None:
        """
        Initialize a BaseComponent object.

        Args:
        - component_spec (ComponentSpec): The specification of the component.
        """
        self.__id: int = 0
        self.__types: List[TypeSpec] = component_spec.get_types()
        self.__type: TypeSpec = self.__types[0]
        self.__component_type: str = component_spec.get_component_type()

    def set_type(self, component_type: str) -> None:
        """
        Set the type of the component.

        Args:
        - component_type (str): The new type of the component.
        """
        self.__type = self._get_type_spec(component_type)

    def get_type(self) -> T:
        """
        Get the type of the component.

        Returns:
        - TypeSpec: The type of the component.
        """
        return self.__type

    def get_component_type(self) -> str:
        """
        Get the component type.

        Returns:
        - str: The type of the component.
        """
        return self.__component_type

    def get_types(self) -> List[T]:
        """
        Get the possible types for this component.

        Returns:
        - List[TypeSpec]: The possible types of the component.
        """
        return self.__types

    def get_id(self) -> int:
        """
        Get the unique identifier of the component.

        Returns:
        - str: The unique identifier of the component.
        """
        return self.__id

    def set_id(self, id: int) -> None:
        """
        Set the unique identifier of the component.

        Args:
        - id (str): The new identifier of the component.
        """
        self.__id = id

    def _get_type_spec(self, component_type: str) -> T:
        """
        Get the type specification for the given component type.

        Args:
        - component_type (str): The type of the component.

        Returns:
        - TypeSpec: The type specification for the component type.

        Raises:
        - ValueError: If the component type is invalid.
        """
        for type_spec in self.__types:
            if type_spec.get_name() == component_type:
                return type_spec
        raise ValueError("Invalid type name.")

    @abstractmethod
    def get_display_text(self) -> str:
        """
        Get the display text of the component.

        Returns:
        - str: The display text of the component.
        """
        pass
