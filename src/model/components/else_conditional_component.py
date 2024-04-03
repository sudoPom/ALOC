from typing import Tuple

from src.model.component_specifications.else_conditional_component_spec import \
    ElseConditionalComponentSpec
from src.model.components.chain_component import ChainComponent
from src.model.components.conditional_component import ConditionalComponent


class ElseConditionalComponent(ConditionalComponent):
    """
    ElseConditionalComponent class represents a conditional component.

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

    def __init__(
        self, conditional_component_spec: ElseConditionalComponentSpec
    ) -> None:
        """
        Initializes a ConditionalComponent object.

        Args:
        - conditional_component_spec (ConditionalComponentSpec): The specification of the conditional component.
        """
        super().__init__(conditional_component_spec)

        self.__else_component: ChainComponent = ChainComponent(
            conditional_component_spec.get_else_spec(), self
        )
        self.add_child(self.__else_component)

    def get_else(self) -> ChainComponent:
        """Retrieves the result component."""
        return self.__else_component

    def reset_id(self, id: int, internal_id: int) -> Tuple[int, int]:
        """
        Resets the ID of the component and its subsequent components in the chain.

        Args:
        - id (int): The new ID to be set.

        Returns:
        - int: The updated ID.
        """
        id, internal_id = super().reset_id(id, internal_id)
        return self.__else_component.reset_id(id, internal_id)

    def to_cola(self) -> str:
        text = super().to_cola()
        else_text = self.__else_component.to_cola()
        return f"{text}\nELSE\n{else_text}"
