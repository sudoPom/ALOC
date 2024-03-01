from typing import Tuple

from src.model.chain_parent import ChainParent
from src.model.component_specifications.conditional_component_spec import \
    ConditionalComponentSpec
from src.model.components.chain_component import ChainComponent
from src.model.components.component import Component


class ConditionalComponent(Component, ChainParent):
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
        Component.__init__(self, conditional_component_spec)
        ChainParent.__init__(self, False)

        self.__condition_component: ChainComponent = ChainComponent(
            conditional_component_spec.get_condition_spec(), self
        )
        self.__result_component: ChainComponent = ChainComponent(
            conditional_component_spec.get_result_spec(), self
        )
        self.add_child(self.__condition_component)
        self.add_child(self.__result_component)

    def get_result(self) -> ChainComponent:
        """Retrieves the result component."""
        return self.__result_component

    def get_condition(self) -> ChainComponent:
        """Retrieves the condition component."""
        return self.__condition_component

    def get_display_text(self) -> str:
        """Retrieves the display text of the component."""
        return ""

    def reset_id(self, id: int, internal_id: int) -> Tuple[int, int]:
        """
        Resets the ID of the component and its subsequent components in the chain.

        Args:
        - id (int): The new ID to be set.

        Returns:
        - int: The updated ID.
        """
        self.set_internal_id(internal_id)
        internal_id += 1
        current_type = self.get_type().get_name()
        if current_type == "if":
            id, internal_id = self.__result_component.reset_id(id, internal_id)
            return self.__condition_component.reset_id(id, internal_id)
        elif current_type == "if then":
            id, internal_id = self.__condition_component.reset_id(id, internal_id)
            return self.__result_component.reset_id(id, internal_id)
        raise ValueError(f"Conditional component has invalid type: {current_type}")

    def delete_chain_component(self, id):
        super().delete_chain_component(id)

    def to_cola(self) -> str:
        current_type = self.get_type().get_name()
        result_text = self.__result_component.to_cola()
        condition_text = self.__condition_component.to_cola()
        if current_type == "if":
            return f"{result_text}\nIF\n{condition_text}"
        elif current_type == "if then":
            return f"IF\n{condition_text}\nTHEN\n{result_text}"
        raise ValueError(f"Conditional component has invalid type: {current_type}")
