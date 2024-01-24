"""
BaseComponent Module

This module defines the BaseComponent class, acting as a parent class to all
Component classes.

Classes:
- BaseComponent: Parent class of all Component classes.

"""


class Component:
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

    def __init__(self, component_id, component_spec):
        """
        Initialize a BaseComponent object.

        Args:
        - id (str): The unique identifier of the component.
        - component_type (str): The type of the component.
        - component_types (set): The set of valid component types.
        """
        self.__id = component_id
        self.__types = component_spec.get_types()
        self.__type = self.__types[0]
        self.__component_type = component_spec.get_component_type()

    def set_type(self, component_type):
        """
        Set the type of the component.

        Args:
        - type (str): The new type of the component.
        """
        self.__type = self._get_type_spec(component_type)

    def get_type(self):
        """
        Get the type of the component.

        Returns:
        - str: The type of the component.
        """
        return self.__type

    def get_component_type(self):
        return self.__component_type

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

    def _get_type_spec(self, component_type):
        for type_spec in self.__types:
            if type_spec.get_name() == component_type:
                return type_spec
        raise ValueError("Invalid type name.")

    def get_display_text(self):
        return None
