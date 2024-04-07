from typing import List

from src.model.chain_parent import ChainParent
from src.model.components.chain_component import ChainComponent
from src.model.components.component import Component


class ComponentCollection:
    """
    ComponentCollection class represents a collection of components.

    Args:
        name (str): The name of the collection.

    """

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__components: List[Component] = []

    def add_component(self, component: Component) -> None:
        """Adds a component to the collection.

        Args:
            component (:obj:`Component`): The component to add to the collection.
        """
        self.__components.append(component)

    def delete_component(self, component_id: int) -> None:
        """Deletes a component from the collection.

        Args:
            component_id (int): The id of the component to delete from the collection.

        Note:
            If the component is not in this collection, nothing happens.
        """
        self.__components = [
            component
            for component in self.__components
            if component.get_internal_id() != component_id
        ]

    def clear(self):
        """
        Deletes all the components from this collection.
        """
        self.__components = []

    def replace_component(self, component_to_replace_with: Component, replace_id):
        """
        Replaces a component with another.

        Args:
            component_to_replace_with (:obj:`Component`): The component to replace with.
            replace_id (int): The id of the component to be replaced.

        Raises:
            ValueError: If there is no such component with :obj:`replace_id`
        """
        if not self.contains_component(replace_id):
            raise ValueError(
                "Treid to replace component with id {replace_id} but it doesn't exist."
            )
        self.__components = [
            component
            if component.get_internal_id() != replace_id
            else component_to_replace_with
            for component in self.__components
        ]

    def get_name(self) -> str:
        """
        Returns the name of the collection.

        Returns:
            str: The name of the collection.
        """
        return self.__name

    def contains_component(self, component_id: int) -> bool:
        """
        Checks if the collection contains a component with the given ID.

        Args:
            component_id (int): The id of the component to check for.

        Returns:
            bool: True if the component is in the collection, false otherwise.
        """
        try:
            self.get_component(component_id)
            return True
        except:
            return False

    def get_component(self, component_id: int) -> Component:
        """
        Returns a component from the collection by its ID.

        Args:
            component_id (int): The id of the component to get from the collection.

        Returns:
            :obj:`Component`: The component requested for.

        Raises:
            ValueError: If the component is not in the collection.
        """
        for component in self.__components:
            if component.get_internal_id() == component_id:
                return component
            if isinstance(component, ChainComponent):
                found_component = self._search_chain_component(component, component_id)
                if found_component is not None:
                    return found_component
            if isinstance(component, ChainParent):
                for child in component.get_children():
                    found_component = self._search_chain_component(child, component_id)
                    if found_component is not None:
                        return found_component
        raise ValueError(f"Component with id {component_id} not found")

    def get_components(self) -> List[Component]:
        """
        Returns all components in the collection.

        Returns:
            :obj:`List[Component]`: All the components in the collection.
        """
        return self.__components

    def _search_chain_component(self, component, component_id):
        current_component = component
        while current_component and current_component.get_internal_id() != component_id:
            current_component = current_component.get_next()
        return current_component
