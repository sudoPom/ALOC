from typing import List

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
        component_ids = [component.get_internal_id() for component in self.__components]
        return component_id in component_ids

    def get_component(self, component_id: str) -> Component:
        """Retrieves a component from the collection by its ID."""
        for component in self.__components:
            if component.get_internal_id() == component_id:
                return component
        raise ValueError("Component not found")

    def get_components(self) -> List[Component]:
        """Retrieves all components in the collection."""
        return self.__components
