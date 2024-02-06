from model.component_specifications.conditional_component_spec import (
    ConditionalComponentSpec,
)
from model.components.chain_component import ChainComponent
from model.components.component import Component


class ConditionalComponent(Component):
    """
    ConditionalComponent class represents a conditional component.

    This class inherits from Component.

    Methods:
    - __init__(conditional_component_spec): Initializes a ConditionalComponent object.
    - get_result(): Retrieves the result component.
    - get_condition(): Retrieves the condition component.
    - get_display_text(): Retrieves the display text of the component.
    - reset_id(id): Resets the ID of the component and its subsequent components.

    Attributes:
    - Inherits all attributes from the Component class.
    """

    def __init__(self, conditional_component_spec: ConditionalComponentSpec) -> None:
        """
        Initializes a ConditionalComponent object.

        Args:
        - conditional_component_spec (ConditionalComponentSpec): The specification of the conditional component.
        """
        super().__init__(conditional_component_spec)

        self.__condition_component: ChainComponent = ChainComponent(
            conditional_component_spec.get_condition_spec()
        )
        self.__result_component: ChainComponent = ChainComponent(
            conditional_component_spec.get_result_spec()
        )

    def get_result(self) -> ChainComponent:
        """Retrieves the result component."""
        return self.__result_component

    def get_condition(self) -> ChainComponent:
        """Retrieves the condition component."""
        return self.__condition_component

    def get_display_text(self) -> str:
        """Retrieves the display text of the component."""
        return ""

    def reset_id(self, id: int) -> int:
        """
        Resets the ID of the component and its subsequent components in the chain.

        Args:
        - id (int): The new ID to be set.

        Returns:
        - int: The updated ID.
        """
        current_type = self.get_type().get_name()
        if current_type == "if":
            id = self.__result_component.reset_id(id)
            return self.__condition_component.reset_id(id)
        elif current_type == "if then":
            id = self.__condition_component.reset_id(id)
            return self.__result_component.reset_id(id)
        else:
            raise ValueError(f"Conditional component has invalid type: {current_type}")
