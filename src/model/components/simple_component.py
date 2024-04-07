from typing import List, Tuple

from src.model.component_attribute import ComponentAttribute
from src.model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from src.model.components.component import Component
from src.model.simple_form_spec import SimpleFormSpec
from src.model.terminal_types.hybrid_terminal import HybridTerminal
from src.model.terminal_types.multi_choice_terminal import MultiChoiceTerminal
from src.model.terminal_types.terminal import TerminalTypeNames


class SimpleComponent(Component):
    """
    Represents a simple component, which can contain multiple, potentially editable attributes.

    Args:
        component_spec (SimpleComponentSpec): The specification of the component.

    """

    def __init__(self, component_spec: SimpleComponentSpec) -> None:
        super().__init__(component_spec)
        self.__attributes = [
            attribute.create_blank() for attribute in component_spec.get_attributes()
        ]

    def get_form(self) -> SimpleFormSpec:
        """
        Gets the current form of the component

        Returns:
            :obj:`FormSpec`: The current form of the component.
        """
        form_spec = super().get_form()
        assert isinstance(form_spec, SimpleFormSpec)
        return form_spec

    def update(self, **kwargs) -> None:
        """
        Update the attributes of the component with the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments representing the updated attributes.
        """
        for key, value in kwargs.items():
            attribute = self.get_attribute(key)
            attribute.set_value(value)

    def get_current_attributes(self) -> List[ComponentAttribute]:
        """
        Get all the components that are currently being displayed.

        Returns:
            :obj:`List[ComponentAttribute]`: List of component attributes.
        """
        type_spec = self._get_form_spec(self.get_form().get_name())
        assert isinstance(type_spec, SimpleFormSpec)
        return [
            attribute
            for attribute in self.__attributes
            if attribute.get_name() in type_spec.get_expected_attributes()
        ]

    def get_attributes(self) -> List[ComponentAttribute]:
        """
        Get a list of components in the simple statement.

        Returns:
            :obj:`List[ComponentAttribute]`: List of component attributes.
        """
        return self.__attributes

    def get_attribute(self, attribute_name) -> ComponentAttribute:
        """
        Get an attribute of the component.

        Args:
            attribute_name (str): The name of the attribute to be fetched.

        Returns:
            :obj:`ComponentAttribute`: The Attribute requested.

        Raises:
            ValueError: If no attribute exists with name :obj:`attribute_name`.
        """
        for attribute in self.get_attributes():
            if attribute.get_name() == attribute_name:
                return attribute
        raise ValueError(
            f"Unsupported attribute name supplied. Requested {attribute_name} when there are only {[attribute.get_name() for attribute in self.get_attributes()]} "
        )

    def get_display_text(self) -> str:
        """
        Get the display text of the component.

        Returns:
            str: The display text of the component.
        """
        component_type = self.get_form()
        format_string = component_type.get_format_string()
        format_params = [
            self._get_component_value(attribute)
            for attribute in component_type.get_expected_attributes()
        ]
        return f"{self.get_textual_id()} {format_string.format(*format_params)}"

    def reset_id(self, id: int, internal_id: int) -> Tuple[int, int]:
        """
        Reset the ID of the component.

        Args:
            id (int): The new ID to be set.

        Returns:
            :obj:`Tuple[int, int]`: The updated ID.
        """
        self.set_id(id)
        self.set_internal_id(internal_id)
        return id + 1, internal_id + 1

    def _get_component_value(self, component_key: str) -> str | Tuple:
        attribute = self.get_attribute(component_key)
        if attribute.get_terminal().get_type() == TerminalTypeNames.HYBRID:
            return self._get_component_hybrid(attribute)
        if attribute.get_terminal().get_type() == TerminalTypeNames.MULTI_CHOICE:
            return self._get_component_multi_choice(attribute)
        return attribute.get_value()

    @staticmethod
    def _get_component_hybrid(attribute: ComponentAttribute) -> str:
        value = attribute.get_value()
        return value[0] if value[0] != HybridTerminal.CUSTOM_OPTION else value[1]

    @staticmethod
    def _get_component_multi_choice(attribute):
        value = attribute.get_value()
        if value == MultiChoiceTerminal.EMPTY_CHOICE:
            return ""
        return value

    def to_cola(self) -> str:
        """
        Converts this component to its textual CoLa form.

        Returns:
            str: The CoLa representation of the component.
        """
        return f"{self.get_display_text()}"
