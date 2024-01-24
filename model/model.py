"""
Model Module

This module defines the Model class, which wraps the Contract class and
exposes commonly used contract operations.

Classes:
- Model: Wraps the Contract class, exposing commonly used contract operations.

"""

import pickle

from model.components.contract import Contract


class Model:
    """
    """

    def __init__(self):
        """
        Initialize a Model object.
        """
        self.__contract = Contract()

    def add_definition(self, definition_type):
        """
        Adds an empty definition to the current contract.

        Args:
        - definition_type: The type of the new definition.
        """
        self.__contract.add_definition(definition_type)

    @staticmethod
    def change_component_type(component, component_type):
        """
        Changes the type of the component.

        Args:
        - component: The definition whose type will be changed.
        - component_type: The new type of the component.
        """
        component.set_type(component_type)

    @staticmethod
    def update_component(definition, update_dict):
        """
        Updates a definition's components.

        Args:
        - definition: The definition to be updated.
        - update_dict: The key-value pairs of the new definition.
        """
        definition.update(**update_dict)

    def delete_component(self, component_id):
        self.__contract.delete_component(component_id)

    def add_component(self, component_spec):
        self.__contract.add_component(component_spec)

    def add_statement(self, statement_type):
        """
        Adds an empty statement to the current contract.

        Args:
        - statement_type: The type of the new statement.
        """
        self.__contract.add_statement(statement_type)

    def add_conditional_statement(self, conditional_statement_type):
        """
        Adds an empty statement to the current contract.

        Args:
        - statement_type: The type of the new statement.
        """
        self.__contract.add_conditional_statement(conditional_statement_type)

    def add_conditional_definition(self, conditional_definition_type):
        """
        Adds an empty statement to the current contract.

        Args:
        - statement_type: The type of the new statement.
        """
        self.__contract.add_conditional_definition(conditional_definition_type)

    def get_contract(self):
        """
        Returns the current contract.

        Returns:
        - Contract: The contract currently being drafted.
        """
        return self.__contract

    def save_contract_file(self, path: str):
        """
        Saves the current contract.

        Args:
        - path (str): The file path of where the contract should be saved.
        """
        contract_data = pickle.dumps(self.__contract, protocol=pickle.HIGHEST_PROTOCOL)
        with open(path, "wb") as file:
            file.write(contract_data)
        print(f"Contract saved to: {path}")
        self.__contract.set_path(path)

    def open_contract_file(self, path: str):
        """
        Loads the contract stored in the file pointed to by path.

        Args:
        - path (str): The file path to retrieve the contract from.
        """
        try:
            with open(path, "rb") as file:
                contract_data = file.read()
                self.__contract = pickle.loads(contract_data)
                print(f"Contract loaded from: {path}")
        except Exception as e:
            print(f"Error loading contract: {e}")

    def create_new_contract(self):
        self.__contract = Contract()
