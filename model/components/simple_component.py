"""
BaseComponent Module

This module defines the BaseComponent class, acting as a parent class to all
Component classes.

Classes:
- BaseComponent: Parent class of all Component classes.

"""
from model.components.component import Component
from view.terminal_types import Terminal


class SimpleComponent(Component):
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

    def __init__(self, component_spec):
        """
        Initialize a BaseComponent object.

        Args:
        - id (str): The unique identifier of the component.
        - component_type (str): The type of the component.
        - component_types (set): The set of valid component types.
        """
        super().__init__(component_spec)
        self.__attributes = component_spec.get_attributes()

    def update(self, **kwargs):
        """
        Update the attributes of the component with the provided keyword
        arguments.

        Args:
        - **kwargs: Keyword arguments representing the updated attributes.
        """
        for key in kwargs:
            attribute = self._get_attribute(key)
            attribute.set_value(kwargs[key])

    def get_current_attributes(self):
        """
        Returns all the components that are currently being displayed.

        Returns:
        - dict: A dictionary containing all components being used (and their
        values)
        """
        expected_attributes = self._get_type_spec(
            self.get_type().get_name()
        ).get_expected_attributes()
        return [
            attribute
            for attribute in self.__attributes
            if attribute.get_name() in expected_attributes
        ]

    def get_attributes(self):
        """
        Get a dictionary of components in the simple statement.

        Returns:
        - dict: A dictionary containing the components of the simple statement.
        """
        return self.__attributes

    def _get_component_value(self, component_key):
        attribute = self._get_attribute(component_key)
        if attribute.get_type() == Terminal.DATE:
            return self._get_component_date(attribute)
        return attribute.get_value()

    def _get_component_date(self, attribute):
        value = attribute.get_value()
        return value[0] if value[0] != "custom date" else f"on the {value[1]}"

    def _get_attribute(self, name):
        for attribute in self.__attributes:
            if attribute.get_name() == name:
                return attribute
        raise ValueError("Invalid attribute name.")

    def _is_valid_type(self, type_name):
        type_names = [t.get_name() for t in self.__types]
        for name in type_names:
            if name == type_name:
                return True
        return False

    def get_display_text(self):
        component_type = self.get_type()
        format_string = component_type.get_format_string()
        format_params = [
            self._get_component_value(attribute)
            for attribute in component_type.get_expected_attributes()
        ]
        format_params.insert(0, self.get_id())
        return format_string.format(*format_params)

    def reset_id(self, id):
        self.set_id(id)
        return id + 1
