"""
Contract Module

This module defines the Contract class, representing a contract in the AST.

Classes:
- Contract: Represents a contract in the AST.

"""

from model.conditional_definition import ConditionalDefinition
from model.conditional_statement import ConditionalStatement
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
        self.__other_components = []
        self.__path = None

    def add_definition(self, definition_type):
        """
        Add a new definition to the contract.

        Args:
        - definition_type (str): The type of the new definition.
        """
        new_definition = SimpleDefinition(self.get_and_increment_id(), definition_type)
        self.__definitions.append(new_definition)
        self.to_cola()

    def add_statement(self, statement_type):
        """
        Add a new statement to the contract.

        Args:
        - statement_type (str): The type of the new statement.
        """
        new_statement = SimpleStatement(self.get_and_increment_id(), statement_type)
        self.__other_components.append(new_statement)

    def add_conditional_statement(self, conditional_statement_type):
        """
        Add a new conditional statement to the contract.

        Args:
        - conditional_type (str): The type of the new conditional statement.
        """
        new_conditional_statement = ConditionalStatement(
            self.get_and_increment_id(),
            conditional_statement_type,
            self.get_and_increment_id(),
            self.get_and_increment_id(),
        )
        self.__other_components.append(new_conditional_statement)

    def add_conditional_definition(self, conditional_definition_type):
        """
        Add a new conditional statement to the contract.

        Args:
        - conditional_type (str): The type of the new conditional definition.
        """
        new_conditional_statement = ConditionalDefinition(
            self.get_and_increment_id(),
            conditional_definition_type,
            self.get_and_increment_id(),
            self.get_and_increment_id(),
        )
        self.__other_components.append(new_conditional_statement)

    def get_definitions(self):
        """
        Get the list of definitions in the contract.

        Returns:
        - list: List of definitions in the contract.
        """
        return self.__definitions

    def get_other_components(self):
        """
        Get the list of non definition components in the contract.

        Returns:
        - list: List of non definition components in the contract.
        """
        return self.__other_components

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

    def update_non_definition_component(self, statement_id, **kwargs):
        """
        Update the attributes of a statement in the contract.

        Args:
        - id (str): The ID of the statement to update.
        - **kwargs: Keyword arguments representing the updated attributes.
        """
        for component in self.__other_components:
            if component.get_id() == statement_id:
                component.update(kwargs)
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

    def delete_non_definition_component(self, component_id):
        """
        Delete a statement from the contract.

        Args:
        - id (str): The ID of the statement to delete.
        """
        self.__other_components = [
            component
            for component in self.__other_components
            if component.get_id() != component_id
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

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path

    def to_cola(self):
        all_text = [definition.get_display_text() for definition in self.__definitions]
        all_text.extend(
            [component.get_display_text() for component in self.__other_components]
        )
        print(" C-AND ".join(all_text))
