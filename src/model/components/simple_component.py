from typing import Any, Dict, List, Tuple

from model.component_attribute import ComponentAttribute
from model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from model.components.component import Component
from model.simple_type_spec import SimpleTypeSpec
from model.terminal_types.terminal import TerminalTypeNames
from view.terminal_types import Terminal


class SimpleComponent(Component):
    """
    Parent class of all component classes.

    Args:
    - component_spec (SimpleComponentSpec): The specification of the component.

    Methods:
    - update(**kwargs): Update the attributes of the component with the provided keyword arguments.
    - get_current_attributes(): Get all the components that are currently being displayed.
    - get_attributes(): Get a dictionary of components in the simple statement.
    - get_display_text(): Get the display text of the component.
    - reset_id(id): Reset the ID of the component.

    Attributes:
    - Inherits all attributes from the Component class.
    """

    def __init__(self, component_spec: SimpleComponentSpec) -> None:
        """
        Initialize a BaseComponent object.

        Args:
        - component_spec (SimpleComponentSpec): The specification of the component.
        """
        super().__init__(component_spec)
        self.__attributes: List[ComponentAttribute] = component_spec.get_attributes()

    def update(self, **kwargs: Any) -> None:
        """
        Update the attributes of the component with the provided keyword arguments.

        Args:
        - **kwargs: Keyword arguments representing the updated attributes.
        """
        for key, value in kwargs.items():
            attribute = self._get_attribute(key)
            attribute.set_value(value)

    def get_current_attributes(self) -> List[ComponentAttribute]:
        """
        Get all the components that are currently being displayed.

        Returns:
        - List[ComponentAttribute]: List of component attributes.
        """
        expected_attributes = self._get_type_spec(
            self.get_type().get_name()
        ).get_expected_attributes()
        return [
            attribute
            for attribute in self.__attributes
            if attribute.get_name() in expected_attributes
        ]

    def get_attributes(self) -> List[ComponentAttribute]:
        """
        Get a list of components in the simple statement.

        Returns:
        - List[ComponentAttribute]: List of component attributes.
        """
        return self.__attributes

    def get_display_text(self) -> str:
        """
        Get the display text of the component.

        Returns:
        - str: The display text of the component.
        """
        component_type = self.get_type()
        format_string = component_type.get_format_string()
        format_params = [
            self._get_component_value(attribute)
            for attribute in component_type.get_expected_attributes()
        ]
        format_params.insert(0, self.get_id())
        return format_string.format(*format_params)

    def reset_id(self, id: int, internal_id: int) -> Tuple[int, int]:
        """
        Reset the ID of the component.

        Args:
        - id (int): The new ID to be set.

        Returns:
        - int: The updated ID.
        """
        self.set_id(id)
        self.set_internal_id(internal_id)
        return id + 1, internal_id + 1

    def _get_component_value(self, component_key: str) -> Any:
        """
        Get the value of the component.

        Args:
        - component_key (str): The key of the component.

        Returns:
        - Any: The value of the component.
        """
        attribute = self._get_attribute(component_key)
        if attribute.get_terminal().get_type() == TerminalTypeNames.DATE:
            return self._get_component_date(attribute)
        return attribute.get_value()

    def _get_component_date(self, attribute: ComponentAttribute) -> str:
        """
        Get the date value of the component.

        Args:
        - attribute (ComponentAttribute): The date attribute.

        Returns:
        - str: The formatted date value.
        """
        value = attribute.get_value()
        return value[0] if value[0] != "custom date" else f"on the {value[1]}"

    def _get_attribute(self, name: str) -> ComponentAttribute:
        """
        Get the attribute by name.

        Args:
        - name (str): The name of the attribute.

        Returns:
        - ComponentAttribute: The attribute object.

        Raises:
        - ValueError: If the attribute name is invalid.
        """
        for attribute in self.__attributes:
            if attribute.get_name() == name:
                return attribute
        raise ValueError("Invalid attribute name.")
