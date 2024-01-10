"""
ConditionalDefinition Module

This module defines the ConditionalDefinition class, representing a conditional
definition in the AST.

Classes:
- ConditionalDefinition: Represents a conditional statement in the AST.

"""
from model.base_component import BaseComponent
from model.simple_condition import SimpleCondition
from model.simple_definition import SimpleDefinition


class ConditionalDefinition(BaseComponent):
    """
    Represents a conditional definition in the AST.
    """

    def __init__(self, conditional_id, conditional_type, definition_id, condition_id):
        """
        Initialize a ConditionalDefinition object.

        Args:
        - condition_id (int): The unique identifier of the condition.
        - condition_type (str): The type of the condition.
        """
        components = {}
        valid_types = {"if", "if_then"}
        super().__init__(conditional_id, conditional_type, valid_types, components)
        self.__definition = SimpleDefinition(definition_id, "subject pair")
        self.__condition = SimpleCondition(condition_id, "subject verb status")

    def get_display_text(self):
        match self.get_type():
            case "if":
                return f"{self.__definition.get_display_text()} if {self.__condition.get_display_text()}"
            case "if_then":
                return f"if {self.__condition.get_display_text()} then {self.__definition.get_display_text()}"
            case _:
                raise ValueError(
                    f"Invalid conditional statement type: {self.get_type()}"
                )

    def get_definition(self):
        return self.__definition

    def get_condition(self):
        return self.__condition
