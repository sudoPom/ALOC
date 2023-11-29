"""
BaseComponent Module

This module defines the BaseComponent class, acting as a parent class to all
Component classes.

Classes:
- BaseComponent: Parent class of all Component classes.

"""
from view.non_terminal_types import ContractNonTerminal
COMPONENT_VALUE_INDEX = 0


class BaseComponent:
    """
    Parent class of all component classes.

    Args:
    - id (str): The unique identifier of the component.
    - component_type (str): The type of the component.
    - component_types (set): The set of valid component types.

    Methods:
    - update(**kwargs): Update the attributes of the component with the
    provided keyword arguments.
    - set_type(type): Set the type of the component.
    - get_type(): Get the type of the component.
    - get_id(): Get the unique identifier of the component.
    - extract_key(kwargs, key, default): Extract the value of a key from
    kwargs, with a default value if the key is not present.
    - throw_if_no_keys_found(kwargs, expected_keys): Throw an error if
    none of the expected keys are found in kwargs.
    """

    def __init__(self, component_id, component_type, component_types, components):
        """
        Initialize a BaseComponent object.

        Args:
        - id (str): The unique identifier of the component.
        - component_type (str): The type of the component.
        - component_types (set): The set of valid component types.
        """
        self.__id = component_id
        self.__type = component_type
        self.__types = component_types
        self.__components = components

    def update(self, **kwargs):
        """
        Update the attributes of the component with the provided keyword
        arguments.

        Args:
        - **kwargs: Keyword arguments representing the updated attributes.
        """
        for key in kwargs:
            if key not in self.__components:
                raise ValueError(
                    f"Invalid key for component: {key}, expected any from {self.__components.keys()}")
            self.__components[key][COMPONENT_VALUE_INDEX] = kwargs[key]

    def set_type(self, component_type):
        """
        Set the type of the component.

        Args:
        - type (str): The new type of the component.
        """
        if component_type not in self.__types:
            raise ValueError(f"Invalid component type, {type}")
        self.__type = type

    def get_current_components(self):
        """
        Returns all the components that are currently being displayed.

        Returns:
        - dict: A dictionary containing all components being used (and their
        values)
        """
        current_components = {}
        for component in self.__components:
            if component in self.__types[self.__type]:
                current_components[component] = self.__components[component]
        return current_components

    def get_components(self):
        """
        Get a dictionary of components in the simple statement.

        Returns:
        - dict: A dictionary containing the components of the simple statement.
        """
        return self.__components

    def get_type(self):
        """
        Get the type of the component.

        Returns:
        - str: The type of the component.
        """
        return self.__type

    def get_types(self):
        """
        Get the possible types for this component.

        Returns:
        - The possible types of the component.
        """
        return self.__types

    def get_id(self):
        """
        Get the unique identifier of the component.

        Returns:
        - str: The unique identifier of the component.
        """
        return self.__id

    def _get_component_value(self, component_key):
        if component_key not in self.__components:
            raise ValueError(f"Invalid component type: {component_key}")
        return self.__components[component_key][0]

    def _get_component_date(self, date_key):
        if date_key not in self.__components:
            raise ValueError(f"Invalid component type: {date_key}")
        date_component = self.__components[date_key]
        if (date_component[1] != ContractNonTerminal.DATE):
            raise ValueError(
                f"Component {date_key} is not a date. It is a {date_component[1]}")
        date = date_component[0]
        return date[0] if date[0] != "custom date" else date[1]
