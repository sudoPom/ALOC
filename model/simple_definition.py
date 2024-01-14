"""
SimpleDefinition Module

This module defines the SimpleDefinition class, representing a simple
definition in the AST.

Classes:
- SimpleDefinition: Represents a simple definition in the AST.

"""
from model.base_component import BaseComponent
from view.non_terminal_types import ContractNonTerminal


class SimpleDefinition(BaseComponent):
    """
    Represents a simple definition in the AST.

    Args:
    - definition_id (str): The unique identifier of the definition.
    - definition_type (str): The type of the definition.
    """

    def __init__(self, definition_id, definition_type):
        """
        Initialize a SimpleDefinition object.

        Args:
        - definition_id (str): The unique identifier of the definition.
        - definition_type (str): The type of the definition.
        """
        components = {
            "subject": ["NAME", ContractNonTerminal.SUBJECT],
            "other_subject": ["DEFINITION", ContractNonTerminal.SUBJECT],
            "numerical_expression": ["0", ContractNonTerminal.NUMERICAL_EXPRESSION],
        }
        valid_types = {
            "subject pair": ["subject", "other_subject"],
            "subject numerical pair": ["subject", "numerical_expression"],
        }
        super().__init__(definition_id, definition_type, valid_types, components)

    def get_display_text(self):
        match self.get_type():
            case "subject pair":
                return f"[{self.get_id()}] {self._get_component_value('subject')} is {self._get_component_value('other_subject')}"
            case "subject numerical pair":
                return f"[{self.get_id()}] {self._get_component_value('subject')} is {self._get_component_value('numerical_expression')}"
            case _:
                raise ValueError(f"Invalid statement type: {self.get_type()}")

    def to_cola(self):
        return self.get_display_text()
