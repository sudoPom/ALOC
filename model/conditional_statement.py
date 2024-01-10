"""
ConditionalStatement Module

This module defines the ConditionalStatement class, representing a conditional
statement in the AST.

Classes:
- ConditionalStatement: Represents a conditional statement in the AST.

"""
from model.base_component import BaseComponent
from model.simple_condition import SimpleCondition
from model.simple_statement import SimpleStatement


class ConditionalStatement(BaseComponent):
    """
    Represents a simple condition in the AST.
    """

    def __init__(self, conditional_id, condition_type, condition_id, statement_id):
        """
        Initialize a ConditionalStatement object.

        Args:
        - conditional_id (int): The unique identifier of the conditional statement.
        - condition_type (str): The type of the condition.
        """
        components = {}
        valid_types = {"if", "if_then"}
        super().__init__(conditional_id, condition_type, valid_types, components)
        self.__statement = SimpleStatement(statement_id, "subject modal")
        self.__condition = SimpleCondition(condition_id, "subject verb status")

    def get_display_text(self):
        match self.get_type():
            case "if":
                return f"{self.__statement.get_display_text()} if {self.__condition.get_display_text()}"
            case "if_then":
                return f"if {self.__condition.get_display_text()} then {self.__statement.get_display_text()}"
            case _:
                raise ValueError(
                    f"Invalid conditional statement type: {self.get_type()}"
                )

    def get_statement(self):
        return self.__statement

    def get_condition(self):
        return self.__condition
