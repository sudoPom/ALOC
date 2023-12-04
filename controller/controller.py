
"""
Controller Module

This module defines the Controller class, which serves as the controller in
the MVC architecture.

Classes:
- Controller: The controller in the MVC architecture.

"""

from model.model import Model


class Controller:
    """
    Controller serves as the controller in the MVC architecture.

    Methods:
    - __init__(model): Initializes a Controller object.
    - get_contract(): Retrieves the current contract from the model.
    - add_new_definition(definition_type): Adds a new definition to the
    contract through the model.
    - change_definition_type(definition, definition_type): Changes the type of
    a definition through the model.
    - update_definition(definition, update_dict): Updates a definition through
    the model.
    - delete_definition(definition_id): Deletes a definition from the contract
    through the model.
    - add_new_statement(statement_type): Adds a new statement to the contract
    through the model.
    - change_statement_type(statement, statement_type): Changes the type of a
    statement through the model.
    - update_statement(statement, update_dict): Updates a statement through
    the model.
    - delete_statement(statement_id): Deletes a statement from the contract
    through the model.

    """

    def __init__(self, model: Model):
        """
        Initializes a Controller object.

        Args:
        - model (Model): The model instance to be associated with the
        controller.
        """
        self.__model = model

    def get_contract(self):
        """
        Retrieves the current contract from the model.

        Returns:
        - Contract: The current contract.
        """
        return self.__model.get_contract()

    def add_new_definition(self, definition_type):
        """
        Adds a new definition to the contract through the model.

        Args:
        - definition_type: The type of the new definition.
        """
        self.__model.add_definition(definition_type)

    @staticmethod
    def change_component_type(component, component_type):
        """
        Changes the type of a definition through the model.

        Args:
        - definition: The definition whose type will be changed.
        - definition_type: The new type of the definition.
        """
        Model.change_component_type(component, component_type)

    @staticmethod
    def update_component(component, update_dict):
        """
        Updates a definition through the model.

        Args:
        - definition: The definition to be updated.
        - update_dict: The key-value pairs of the new definition.
        """
        Model.update_component(component, update_dict)

    def delete_definition(self, definition_id):
        """
        Deletes a definition from the contract through the model.

        Args:
        - definition_id: The ID of the definition to be deleted.
        """
        self.__model.delete_definition(definition_id)

    def add_new_statement(self, statement_type):
        """
        Adds a new statement to the contract through the model.

        Args:
        - statement_type: The type of the new statement.
        """
        self.__model.add_statement(statement_type)

    def delete_statement(self, statement_id):
        """
        Deletes a statement from the contract through the model.

        Args:
        - statement_id: The ID of the statement to be deleted.
        """
        self.__model.delete_statement(statement_id)

    @staticmethod
    def extend_component_chain(component):
        component.add_next()

    def set_logic_operator(self, component, operator):
        component.set_logic_operator(operator)

    @staticmethod
    def delete_next_component_from_chain(component):
        component.delete_next_component()
