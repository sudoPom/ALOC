"""
Contract Module

This module defines the Contract class, representing a contract in the AST.

Classes:
- Contract: Represents a contract in the AST.

"""


class Contract:
    """
    Represents a contract in the AST.

    Methods:
    - __init__(): Initialize a Contract object.
    - add_definition(definition_type): Add a new definition to the contract.
    - add_statement(statement_type): Add a new statement to the contract.
    - get_definitions(): Get the list of definitions in the contract.
    - get_statements(): Get the list of statements in the contract.
    - update_definition(id, **kwargs): Update the attributes of a definition
    in the contract.
    - update_statement(id, **kwargs): Update the attributes of a statement in
    the contract.
    - delete_definition(id): Delete a definition from the contract.
    - delete_statement(id): Delete a statement from the contract.
    - get_and_increment_id(): Get the current ID counter and increment it.

    """

    def __init__(self, component_collections, component_types):
        """
        Initialize a Contract object.
        """
        self.__component_collections = component_collections
        self.__component_types = component_types
        self.__path = ""

    def delete_component(self, component_id):
        for component_collection in self.__component_collections:
            if component_collection.contains_component(component_id):
                component_collection.delete_component(component_id)
        self.reset_ids()

    def update_component(self, component_id, **kwargs):
        for component_collection in self.__component_collections:
            if component_collection.contains_component(component_id):
                component = component_collection.get_component(component_id)
                component.update(kwargs)
                return
        raise ValueError(f"This statement does not exist! {component_id}")

    def add_component(self, component_spec):
        component_collection = self._get_component_collection(component_spec)
        component_type = self.__component_types[component_spec.get_component_type()]
        component = component_type(component_spec)
        component_collection.add_component(component)
        self.reset_ids()

    def get_component_collections(self):
        return self.__component_collections

    def _get_component_collection(self, component_spec):
        component_collection_name = component_spec.get_location()
        for component_collection in self.__component_collections:
            if component_collection.get_name() == component_collection_name:
                return component_collection
        raise ValueError(f"This collection doesn't exist! {component_collection_name}")

    def get_path(self) -> str:
        return self.__path

    def set_path(self, path):
        self.__path = path

    def reset_ids(self):
        current_id = 0
        for component_collection in self.__component_collections:
            for component in component_collection.get_components():
                current_id = component.reset_id(current_id)
