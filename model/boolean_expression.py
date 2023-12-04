
"""
BooleanExpression Module

This module defines the Condition class, representing a simple
condition in the AST.

Classes:
- BooleanExpression: Represents a boolean expression in the AST.

"""
from model.base_component import BaseComponent
from view.non_terminal_types import ContractNonTerminal


class BooleanExpression(BaseComponent):
    """
    Represents a boolean expression in the AST.
    """

    def __init__(self, expression_id, expression_type):
        """
        Initialize a BooleanExpression object.

        Args:
        - expression_id (str): The unique identifier of the boolean_expression.
        - expression_type (str): The type of the condition.
        """
        components = {
            "subject": ["NAME", ContractNonTerminal.SUBJECT],
            "verb_status": ["delivered", ContractNonTerminal.VERB_STATUS],
            "comparison": ["more than", ContractNonTerminal.COMPARISON],
            "other_subject": ["some thing", ContractNonTerminal.SUBJECT]
        }
        valid_types = {
            "subject_verb": [
                "subject",
                "verb_status",
                "comparison",
                "other_subject"
            ],
        }
        super().__init__(
            expression_id, expression_type, valid_types, components
        )

    def get_display_text(self):
        return f"{self._get_component_date('subject')} {self._get_component_date('verb_status')} {self._get_component_date('comparison')} {self._get_component_date('other_subject')}"
