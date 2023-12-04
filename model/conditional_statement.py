"""
ConditionalStatement Module

This module defines the ConditionalStatement class, representing a conditional
statement in the AST.

Classes:
- ConditionalStatement: Represents a conditional statement in the AST.

"""
from model.base_component import BaseComponent
from model.simple_statement import SimpleStatement
from model.simple_condition import SimpleCondition


class ConditionalStatement(BaseComponent):
    """
    Represents a simple condition in the AST.
    """

    def __init__(self, condition_id, condition_type):
        """
        Initialize a ConditionalStatement object.

        Args:
        - condition_id (int): The unique identifier of the condition.
        - condition_type (str): The type of the condition.
        """
        components = {
        }
        valid_types = {
            "if",
            "if_then"
        }
        super().__init__(
            condition_id, condition_type, valid_types, components
        )
        self._statement = SimpleStatement(0, "subject modal")
        self._condition = SimpleCondition(0, "subject verb status")

    def get_display_text(self):
        match self.get_type():
            case "if":
                return f'{self._statement.get_display_text()} if {self._condition.get_display_text()}'
            case "if_then":
                return f'if {self._condition.get_display_text()} then {self._statement.get_display_text}'
            case _:
                raise ValueError(
                    f"Invalid conditional statement type: {self.get_type()}")
        pass
