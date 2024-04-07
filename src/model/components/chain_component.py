from typing import Tuple

from src.model.chain_parent import ChainParent
from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.components.simple_component import SimpleComponent


class ChainComponent(SimpleComponent):
    """
    The ChainComponent class represents a component in a chain of components.

    Args:
        component_spec (:obj:`ChainComponentSpec`): The specification of the component.
        parent (:obj:`ChainParent`): The parent component of the chain.
    """

    def __init__(self, component_spec: ChainComponentSpec, parent: ChainParent) -> None:
        super().__init__(component_spec)
        self.__component_spec: ChainComponentSpec = component_spec
        self.__next = None
        self.__parent: ChainParent = parent
        self.__linking_attribute = component_spec.get_linking_attribute()

    def add_next(self) -> None:
        """Adds another component to the chain."""
        old_next = self.__next
        new_next = ChainComponent(self.__component_spec.create_blank(), self.__parent)
        self.set_next(new_next)
        new_next.set_next(old_next)

    def set_next(self, next_component: "ChainComponent | None") -> None:
        """
        Sets the next component in the chain.

        Args:
            next_component (:obj:`ChainComponent`, optional): The next component in the chain.
        """
        self.__next = next_component

    def get_next(self) -> "ChainComponent | None":
        """Retrieves the next component in the chain.

        Returns:
            :obj:`ChainComponent | None` : The next component in the chain.
        """
        return self.__next

    def delete(self) -> None:
        """
        Attempts to delete this component from the chain.

        Note:
            The object will not be deleted if it is the only component in the chain
            and the parent component has the :obj:`allow_chain_deletion` attribute
            set to True.
        """
        self.__parent.delete_chain_component(self.get_internal_id())

    def get_chain_component(
        self, internal_id: int, prev_component: "ChainComponent | None" = None
    ) -> Tuple:
        """
        Gets the predecessor component and the component of a component.

        Args:
            internal_id (int): The id of the component to search for.
            prev_component (:obj:`ChainComponent`, optional): The last component checked.

        Returns:
            :obj:`tuple`: The component with internal id and its predecessor, or None and the last component
            in the chain if it doesn't exist in the chain.
        """
        if internal_id == self.get_internal_id():
            return prev_component, self
        next_component = self.get_next()
        if next_component:
            return next_component.get_chain_component(internal_id, self)
        return self, None

    def get_display_text(self) -> str:
        """
        Gets the display text of the component.

        Returns:
            str: The display text of the component.
        """
        text: str = super().get_display_text()
        if not self.__next:
            return text
        attribute_value = self.get_attribute(self.__linking_attribute).get_value()
        assert type(attribute_value) is str
        text += f" {attribute_value}"
        return text

    def get_current_attributes(self):
        """
        Gets all the attributes that are present in the current form of the component.

        Returns:
            :obj:`List[ComponentAttribute]`: List of all attributes currently in use by the component.
        """
        attributes = super().get_current_attributes()
        attributes.append(self.get_attribute(self.__linking_attribute))
        return attributes

    def reset_id(self, id: int, internal_id: int) -> Tuple[int, int]:
        """
        Resets the IDs of the component and its subsequent components in the chain.

        Args:
            id (int): The new ID to be set.
            internal_id (int): The new internal ID to be set.

        Returns:
            The updated ID.
        """
        self.set_id(id)
        self.set_internal_id(internal_id)
        id += 1
        internal_id += 1
        if self.__next:
            return self.__next.reset_id(id, internal_id)
        return id, internal_id

    def to_cola(self):
        """
        Converts this component to its textual CoLa form.

        Returns:
            str: The CoLa representation of the component.
        """
        text = f"{self.get_display_text()}"
        current_component = self.get_next()
        while current_component:
            text += "\n"
            text += f"{current_component.get_display_text()}"
            current_component = current_component.get_next()
        return text
