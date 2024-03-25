from typing import Dict, List, Type

from src.model.chain_parent import ChainParent
from src.model.component_collection import ComponentCollection
from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.component_specifications.component_spec import ComponentSpec
from src.model.components.chain_component import ChainComponent
from src.model.components.component import Component
from src.model.components.simple_component import SimpleComponent
from src.model.constants import Constants


class Contract(ChainParent):
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
        ChainParent.__init__(self, True)
        self.__component_collections: List[ComponentCollection] = component_collections
        self.__component_types: Dict[str, Type[Component]] = component_types
        self.__path: str = ""

    def delete_component(self, component_id: int) -> None:
        """Delete a component from the contract."""
        for component_collection in self.__component_collections:
            if component_collection.contains_component(component_id):
                component_collection.delete_component(component_id)
                return
        raise ValueError(
            f"Tried to delete component with id {component_id} but it doesn't exist."
        )

    def update_component(self, component_id: int, **kwargs) -> None:
        """Update the attributes of a component in the contract."""
        for component_collection in self.__component_collections:
            if component_collection.contains_component(component_id):
                component = component_collection.get_component(component_id)
                assert isinstance(component, SimpleComponent)
                component.update(**kwargs)
                return
        raise ValueError(f"This statement does not exist! {component_id}")

    def add_component(self, component_spec: ComponentSpec) -> None:
        """Add a new component to the contract."""
        component_collection = self._get_component_collection(
            component_spec.get_location()
        )
        component_type = self.__component_types[component_spec.get_component_type()]
        if component_spec.get_component_type() == "chain_component":
            assert isinstance(component_spec, ChainComponentSpec)
            component = ChainComponent(component_spec, self)
            self.add_child(component)
        else:
            component = component_type(component_spec)
        component_collection.add_component(component)

    def get_component_collections(self) -> List[ComponentCollection]:
        """Get the list of component collections in the contract."""
        return self.__component_collections

    def _get_component_collection(
        self, component_collection_name: str
    ) -> ComponentCollection:
        """Get the component collection for the given component specification."""
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
        current_internal_id = 0
        for component_collection in self.__component_collections:
            for component in component_collection.get_components():
                current_id, current_internal_id = component.reset_id(
                    current_id, current_internal_id
                )

    def delete_chain_component(self, id):
        new_first_element = super().delete_chain_component(id)
        if new_first_element:
            component_collection_name = new_first_element.get_location()
            component_collection = self._get_component_collection(
                component_collection_name
            )
            component_collection.replace_component(new_first_element, id)
        else:
            self.delete_component(id)
        self.reset_ids()

    def to_cola(self):
        component_texts = []
        for component_collection in self.get_component_collections():
            components = component_collection.get_components()
            component_texts += [component.to_cola() for component in components]
        return f"\n{Constants.COMPONENT_JOINER}\n".join(component_texts)
