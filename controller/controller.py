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

    def __init__(self, model: Model, component_specs):
        """
        Initializes a Controller object.

        Args:
        - model (Model): The model instance to be associated with the
        controller.
        """
        self.__model = model
        self.__component_specs = component_specs

    def get_contract_path(self):
        return self.__model.get_contract().get_path()

    def save_contract(self, path):
        self.__model.save_contract_file(path)

    def load_contract(self, path):
        self.__model.open_contract_file(path)

    def create_new_contract(self):
        self.__model.create_new_contract()

    def get_contract(self):
        """
        Retrieves the current contract from the model.

        Returns:
        - Contract: The current contract.
        """
        return self.__model.get_contract()

    def add_new_component(self, component):
        component_spec = self.__component_specs[component]
        self.__model.add_component(component_spec)

    def delete_component(self, component_id):
        self.__model.delete_component(component_id)

    def get_contract_component_names(self):
        components = list(self.__component_specs.keys())
        return [
            component
            for component in components
            if self.__component_specs[component].get_location() != "none"
        ]

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

    def extend_chain_component(self, component):
        self.__model.extend_chain_component(component)
