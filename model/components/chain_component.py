from model.component_specifications.chain_component_spec import ChainComponentSpec
from model.components.simple_component import SimpleComponent


class ChainComponent(SimpleComponent):
    """
    ChainComponent class represents a component in a chain of components.

    This class inherits from SimpleComponent.

    Methods:
    - __init__(component_spec): Initializes a ChainComponent object.
    - add_next(): Adds a next component to the chain.
    - set_next(next): Sets the next component in the chain.
    - get_next(): Retrieves the next component in the chain.
    - delete_next_condition(): Deletes the condition of the next component in the chain.
    - get_next_component(): Retrieves the next component in the chain.
    - get_display_text(): Retrieves the display text of the component.
    - reset_id(id): Resets the ID of the component and its subsequent components in the chain.

    Attributes:
    - Inherits all attributes from the SimpleComponent class.
    """

    def __init__(self, component_spec: ChainComponentSpec) -> None:
        """
        Initializes a ChainComponent object.

        Args:
        - component_spec (ChainComponentSpec): The specification of the component.
        """
        super().__init__(component_spec)
        self.__component_spec: ChainComponentSpec = component_spec
        self.__next: ChainComponent | None = None

    def add_next(self) -> None:
        """Adds a next component to the chain."""
        old_next = self.__next
        self.__next = ChainComponent(self.__component_spec)
        self.__next.set_next(old_next)

    def set_next(self, next_component: "ChainComponent | None") -> None:
        """
        Sets the next component in the chain.

        Args:
        - next_component (ChainComponent): The next component in the chain.
        """
        self.__next = next_component

    def get_next(self) -> "ChainComponent | None":
        """Retrieves the next component in the chain."""
        return self.__next

    def delete_next_condition(self) -> None:
        """Deletes the condition of the next component in the chain."""
        if self.__next is None:
            return
        self.__next = self.__next.get_next_component()

    def get_next_component(self) -> "ChainComponent | None":
        """Retrieves the next component in the chain."""
        return self.__next

    def get_display_text(self) -> str:
        """Retrieves the display text of the component."""
        text: str = super().get_display_text()
        if not self.__next:
            text = " ".join(text.split(" ")[:-1])
        return text

    def reset_id(self, id: int) -> int:
        """
        Resets the ID of the component and its subsequent components in the chain.

        Args:
        - id (int): The new ID to be set.

        Returns:
        - int: The updated ID.
        """
        self.set_id(id)
        id += 1
        if self.__next:
            return self.__next.reset_id(id)
        return id
