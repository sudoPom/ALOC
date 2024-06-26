from typing import Dict, List

from src.model.component_specifications.component_spec import ComponentSpec
from src.model.components.contract import Contract
from src.model.model import Model


class Controller:
    """
    Class for sending control messages between the view and model of ALOC.
    """

    def __init__(self, model: Model, component_specs: Dict[str, ComponentSpec]):
        """
        Initializes a Controller object.

        Args:
            model (Model): The model instance to be associated with the controller.
            component_specs (dict): A dictionary mapping component names to
                component specifications.
        """
        self.__model = model
        self.__component_specs = component_specs

    def get_contract_path(self) -> str:
        """
        Retrieves the path of the current contract.

        Returns:
        - str: The path of the current contract.
        """
        return self.__model.get_contract().get_path()

    def save_contract(self, path) -> None:
        """
        Saves the current contract to the specified path.

        Args:
            path (str): The path where the contract will be saved.
        """
        self.__model.save_contract_file(path)

    def load_contract(self, path) -> None:
        """
        Loads a contract from the specified path.

        Args:
            path (str): The path from where the contract will be loaded.
        """
        self.__model.open_contract_file(path)

    def export_to_cola(self, path) -> None:
        """
        Exports the current contract to CoLa and saves it to the specified path.

        Args:
            path (str): The path to store the exported CoLa.
        """
        self.__model.export_to_cola(path)

    def create_new_contract(self) -> None:
        """Creates a new contract."""
        self.__model.create_new_contract()

    def get_contract(self) -> Contract:
        """
        Retrieves the current contract from the model.

        Returns:
            The current contract being drafted.
        """
        return self.__model.get_contract()

    def add_new_component(self, component_name) -> None:
        """
        Adds a new component to the contract.

        Args:
            component_name (str): The name of the component to be added.
        """
        component_spec = self.__component_specs[component_name]
        self.__model.add_component(component_spec)

    def delete_component(self, component_id: int) -> None:
        """
        Deletes a component from the contract.

        Args:
            component_id (int): The ID of the component to be deleted.
        """
        self.__model.delete_component(component_id)

    def get_contract_component_names(self) -> List[str]:
        """
        Retrieves the names of contract components.

        Returns:
            A list of contract component names.
        """
        components = list(self.__component_specs.keys())
        return [
            component
            for component in components
            if self.__component_specs[component].get_location() != "none"
        ]

    def get_contract_as_cola(self) -> str:
        """
        Gets the textual representation of the contract.

        Returns:
            str: The textual representation of the contract.
        """
        return self.__model.get_contract().to_cola()

    def change_component_form(self, component_id: int, component_form) -> None:
        """
        Changes the form of a component.

        Args:
            component_id (int): The id component whose type will be changed.
            component_form (str): The name of the new form of the component.
        """
        self.__model.change_component_form(component_id, component_form)

    def update_component(self, component_id: int, update_dict) -> None:
        """
        Updates a component.

        Args:
            component_id : The id of the component to be updated.
            update_dict: The key-value pairs of the new component.
        """
        self.__model.update_component(component_id, update_dict)

    def extend_chain_component(self, component_id: int) -> None:
        """
        Extends a chain component in the contract.

        Args:
            component_id (int): The id of the chain component to be extended.
        """
        self.__model.extend_chain_component(component_id)

    def reset_ids(self):
        """
        Notifies the model to reset the ids of all components in the contract.
        """
        self.__model.reset_ids()
