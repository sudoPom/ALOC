
"""
Model Module

This module defines the Model class, which wraps the Contract class and
exposes commonly used contract operations.

Classes:
- Model: Wraps the Contract class, exposing commonly used contract operations.

"""

from model.contract import Contract


class Model:
    """
    Model wraps the Contract class, exposing commonly used contract operations.

    Methods:
    - __init__(): Initialize a Model object.
    - add_definition(definition_type): Adds an empty definition to the current
    contract.
    - change_component_type(definition, definition_type): Changes the type of
    the definition.
    - update_component(definition, update_dict): Updates a definition's
    components.
    - delete_definition(definition_id): Deletes a definition from the contract.
    - add_statement(statement_type): Adds an empty statement to the current
    contract.
    - delete_statement(statement_id): Deletes a statement from the current
    contract.
    - get_contract(): Returns the current contract.
    - save_contract_file(path): Saves the current contract.
    - open_contract_file(path): Loads the contract stored in the file pointed
    to by path.

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
    def change_type(component, component_type):
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

    def delete_definition(self, definition_id):
        """
        Deletes a definition from the contract.

        Args:
        - definition_id: The ID of the definition to be deleted.
        """
        self.__contract.delete_definition(definition_id)

    def add_statement(self, statement_type):
        """
        Adds an empty statement to the current contract.

        Args:
        - statement_type: The type of the new statement.
        """
        self.__contract.add_statement(statement_type)

    def delete_statement(self, statement_id):
        """
        Deletes a statement from the current contract.

        Args:
        - statement_id: The ID of the statement to be deleted.
        """
        self.__contract.delete_statement(statement_id)

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
        # Implementation for saving the contract goes here

    def open_contract_file(self, path: str):
        """
        Loads the contract stored in the file pointed to by path.

        Args:
        - path (str): The file path to retrieve the contract from.
        """
        # Implementation for opening and loading the contract goes here
