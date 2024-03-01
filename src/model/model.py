import pickle
from typing import Dict, List, Type

from model.component_collection import ComponentCollection
from model.components.component import Component
from model.components.contract import Contract


class Model:
    """
    Wraps the Contract class, exposing commonly used contract operations.

    Methods:
    - __init__(component_collections, component_spec_pairs): Initializes a Model object.
    - change_component_type(component, component_type): Changes the type of the component.
    - update_component(component, update_dict): Updates a component's attributes.
    - delete_component(component_id): Deletes a component from the contract.
    - add_component(component_spec): Adds a component to the contract.
    - extend_chain_component(component): Extends a chain component in the contract.
    - get_contract(): Retrieves the current contract.
    - save_contract_file(path): Saves the current contract to a file.
    - open_contract_file(path): Loads a contract from a file.
    - create_new_contract(): Creates a new contract.
    """

    def __init__(
        self,
        component_collections: List[ComponentCollection],
        component_spec_pairs: Dict[str, Type[Component]],
    ) -> None:
        """
        Initializes a Model object.

        Args:
        - component_collections (List[ComponentCollection]): A list of component collections.
        - component_spec_pairs (List[ComponentSpecPair]): A list of component specification pairs.
        """
        self.__component_collections: List[ComponentCollection] = component_collections
        self.__component_spec_pairs: Dict[str, Type[Component]] = component_spec_pairs
        self.create_new_contract()

    @staticmethod
    def change_component_type(component, component_type):
        """
        Changes the type of the component.

        Args:
        - component: The component whose type will be changed.
        - component_type: The new type of the component.
        """
        component.set_type(component_type)

    @staticmethod
    def update_component(component, update_dict):
        """
        Updates a component's attributes.

        Args:
        - component: The component to be updated.
        - update_dict: A dictionary containing the updated attributes.
        """
        component.update(**update_dict)

    def delete_component(self, component_id):
        """
        Deletes a component from the contract.

        Args:
        - component_id: The ID of the component to be deleted.
        """
        self.__contract.delete_component(component_id)
        self.__contract.reset_ids()

    def add_component(self, component_spec):
        """
        Adds a component to the contract.

        Args:
        - component_spec: The component specification to be added.
        """
        self.__contract.add_component(component_spec)
        self.__contract.reset_ids()

    def extend_chain_component(self, component):
        """
        Extends a chain component in the contract.

        Args:
        - component: The chain component to be extended.
        """
        component.add_next()
        self.__contract.reset_ids()

    def get_contract(self) -> Contract:
        """
        Retrieves the current contract.

        Returns:
        - Contract: The current contract.
        """
        return self.__contract

    def save_contract_file(self, path: str) -> None:
        """
        Saves the current contract to a file.

        Args:
        - path (str): The file path where the contract should be saved.
        """
        contract_data = pickle.dumps(self.__contract, protocol=pickle.HIGHEST_PROTOCOL)
        with open(path, "wb") as file:
            file.write(contract_data)
        self.__contract.set_path(path)

    def open_contract_file(self, path: str) -> None:
        """
        Loads a contract from a file.

        Args:
        - path (str): The file path to load the contract from.
        """
        try:
            with open(path, "rb") as file:
                contract_data = file.read()
                self.__contract = pickle.loads(contract_data)
        except Exception as e:
            print(f"Error loading contract: {e}")

    def create_new_contract(self) -> Contract:
        """
        Creates a new contract.

        Returns:
        - Contract: The newly created contract.
        """
        for component_collection in self.__component_collections:
            component_collection.clear()
        self.__contract = Contract(
            self.__component_collections, self.__component_spec_pairs
        )
        return Contract(self.__component_collections, self.__component_spec_pairs)

    def export_to_cola(self, path: str):
        """
        Exports the contract to CoLa and saves it.

        Args:
        - path (str): The file path to save the CoLa to.
        """
        try:
            cola = self.__contract.to_cola()
            with open(path, "w") as file:
                file.write(cola)
        except Exception as e:
            print(f"Error exporting to contract: {e}")

    def reset_ids(self):
        self.__contract.reset_ids()
