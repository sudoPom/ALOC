from typing import List

from src.model.chain_parent import ChainParent
from src.model.components.chain_component import ChainComponent
from src.model.components.component import Component


class ComponentCollection:
    """
    Represents a collection of components.

    Methods:
    - __init__(name): Initializes a ComponentCollection object.
    - add_component(component): Adds a component to the collection.
    - delete_component(component_id): Deletes a component from the collection.
    - get_name(): Retrieves the name of the collection.
    - contains_component(component_id): Checks if the collection contains a component with the given ID.
    - get_component(component_id): Retrieves a component from the collection by its ID.
    - get_components(): Retrieves all components in the collection.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a ComponentCollection object.

        Args:
        - name (str): The name of the collection.
        """
        self.__name: str = name
        self.__components: List[Component] = []

    def add_component(self, component: Component) -> None:
        """Adds a component to the collection."""
        self.__components.append(component)

    def delete_component(self, component_id: int) -> None:
        """Deletes a component from the collection."""
        self.__components = [
            component
            for component in self.__components
            if component.get_internal_id() != component_id
        ]

    def clear(self):
        self.__components = []

    def replace_component(self, component_to_replace_with, replace_id):
        self.__components = [
            component
            if component.get_internal_id() != replace_id
            else component_to_replace_with
            for component in self.__components
        ]

    def get_name(self) -> str:
        """Retrieves the name of the collection."""
        return self.__name

    def contains_component(self, component_id: int) -> bool:
        """Checks if the collection contains a component with the given ID."""
        try:
            self.get_component(component_id)
            return True
        except:
            return False

    def get_component(self, component_id: int) -> Component:
        """Retrieves a component from the collection by its ID."""
        for component in self.__components:
            if component.get_internal_id() == component_id:
                return component
            if isinstance(component, ChainComponent):
                found_component = self.search_chain_component(component, component_id)
                if found_component is not None:
                    return found_component
            if isinstance(component, ChainParent):
                for child in component.get_children():
                    found_component = self.search_chain_component(child, component_id)
                    if found_component is not None:
                        return found_component
        raise ValueError(f"Component with id {component_id} not found")

    def get_components(self) -> List[Component]:
        """Retrieves all components in the collection."""
        return self.__components

    def search_chain_component(self, component, component_id):
        current_component = component
        while current_component and current_component.get_internal_id() != component_id:
            current_component = current_component.get_next()
        return current_component
