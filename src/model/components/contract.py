from typing import Dict, List, Type

from model.component_collection import ComponentCollection
from model.component_specifications.component_spec import ComponentSpec
from model.components.component import Component


class Contract:
    """
    Represents a contract in the AST.

    Methods:
    - __init__(component_collections, component_types): Initialize a Contract object.
    - delete_component(component_id): Delete a component from the contract.
    - update_component(component_id, **kwargs): Update the attributes of a component in the contract.
    - add_component(component_spec): Add a new component to the contract.
    - get_component_collections(): Get the list of component collections in the contract.
    - get_path(): Get the path of the contract.
    - set_path(path): Set the path of the contract.
    - reset_ids(): Reset the IDs of all components in the contract.
    """

    def __init__(
        self,
        component_collections: List[ComponentCollection],
        component_types: Dict[str, Type[Component]],
    ) -> None:
        """
        Initialize a Contract object.

        Args:
        - component_collections (List[ComponentCollection]): List of component collections in the contract.
        - component_types (Dict[str, ComponentType]): Dictionary of component types.
        """
        self.__component_collections: List[ComponentCollection] = component_collections
        self.__component_types: Dict[str, Type[Component]] = component_types
        self.__path: str = ""

    def delete_component(self, component_id: str) -> None:
        """Delete a component from the contract."""
        for component_collection in self.__component_collections:
            if component_collection.contains_component(component_id):
                component_collection.delete_component(component_id)
        self.reset_ids()

    def update_component(self, component_id: str, **kwargs) -> None:
        """Update the attributes of a component in the contract."""
        for component_collection in self.__component_collections:
            if component_collection.contains_component(component_id):
                component = component_collection.get_component(component_id)
                component.update(kwargs)
                return
        raise ValueError(f"This statement does not exist! {component_id}")

    def add_component(self, component_spec: ComponentSpec) -> None:
        """Add a new component to the contract."""
        component_collection = self._get_component_collection(component_spec)
        component_type = self.__component_types[component_spec.get_component_type()]
        component = component_type(component_spec)
        component_collection.add_component(component)
        self.reset_ids()

    def get_component_collections(self) -> List[ComponentCollection]:
        """Get the list of component collections in the contract."""
        return self.__component_collections

    def _get_component_collection(
        self, component_spec: ComponentSpec
    ) -> ComponentCollection:
        """Get the component collection for the given component specification."""
        component_collection_name = component_spec.get_location()
        for component_collection in self.__component_collections:
            if component_collection.get_name() == component_collection_name:
                return component_collection
        raise ValueError(f"This collection doesn't exist! {component_collection_name}")

    def get_path(self) -> str:
        """Get the path of the contract."""
        return self.__path

    def set_path(self, path: str) -> None:
        """Set the path of the contract."""
        self.__path = path

    def reset_ids(self) -> None:
        """Reset the IDs of all components in the contract."""
        current_id = 0
        for component_collection in self.__component_collections:
            for component in component_collection.get_components():
                current_id = component.reset_id(current_id)
