"""
Contract Module

This module defines the Contract class, representing a contract in the AST.

Classes:
- Contract: Represents a contract in the AST.

"""

from model.simple_definition import SimpleDefinition
from model.simple_statement import SimpleStatement


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

    def __init__(self):
        """
        Initialize a Contract object.
        """
        self.__id_counter = 0
        self.__definitions = []
        self.__statements = []

    def add_definition(self, definition_type):
        """
        Add a new definition to the contract.

        Args:
        - definition_type (str): The type of the new definition.
        """
        new_definition = SimpleDefinition(
            self.get_and_increment_id(), definition_type)
        self.__definitions.append(new_definition)

    def add_statement(self, statement_type):
        """
        Add a new statement to the contract.

        Args:
        - statement_type (str): The type of the new statement.
        """
        new_statement = SimpleStatement(
            self.get_and_increment_id(), statement_type)
        self.__statements.append(new_statement)

    def get_definitions(self):
        """
        Get the list of definitions in the contract.

        Returns:
        - list: List of definitions in the contract.
        """
        return self.__definitions

    def get_statements(self):
        """
        Get the list of statements in the contract.

        Returns:
        - list: List of statements in the contract.
        """
        return self.__statements

    def update_definition(self, definition_id, **kwargs):
        """
        Update the attributes of a definition in the contract.

        Args:
        - id (str): The ID of the definition to update.
        - **kwargs: Keyword arguments representing the updated attributes.
        """
        for definition in self.__definitions:
            if definition.get_id() == definition_id:
                definition.update(kwargs)
                return
        raise ValueError(f"This definition does not exist! {id}")

    def update_statement(self, statement_id, **kwargs):
        """
        Update the attributes of a statement in the contract.

        Args:
        - id (str): The ID of the statement to update.
        - **kwargs: Keyword arguments representing the updated attributes.
        """
        for statement in self.__statements:
            if statement.get_id() == statement_id:
                statement.update(kwargs)
                return
        raise ValueError(f"This statement does not exist! {id}")

    def delete_definition(self, definition_id):
        """
        Delete a definition from the contract.

        Args:
        - id (str): The ID of the definition to delete.
        """
        self.__definitions = [
            definition
            for definition in self.__definitions
            if definition.get_id() != definition_id
        ]

    def delete_statement(self, definition_id):
        """
        Delete a statement from the contract.

        Args:
        - id (str): The ID of the statement to delete.
        """
        self.__statements = [
            statement
            for statement in self.__statements
            if statement.get_id() != definition_id
        ]

    def get_and_increment_id(self):
        """
        Get the current ID counter and increment it.

        Returns:
        - int: The current value of the ID counter.
        """
        out = self.__id_counter
        self.__id_counter += 1
        return out
