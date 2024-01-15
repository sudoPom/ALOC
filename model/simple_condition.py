"""
SimpleCondition Module

This module defines the Condition class, representing a simple
condition in the AST.

Classes:
- SimpleCondition: Represents a simple definition in the AST.

"""
from model.base_chain import BaseChain
from model.base_component import BaseComponent
from view.non_terminal_types import ContractNonTerminal


class SimpleCondition(BaseComponent, BaseChain):
    """
    Represents a simple condition in the AST.
    """

    def __init__(self, condition_id, condition_type):
        """
        Initialize a SimpleCondition object.

        Args:
        - condition_id (int): The unique identifier of the condition.
        - condition_type (str): The type of the condition.
        """
        components = {
            "holds": ["it is the case that", ContractNonTerminal.HOLDS],
            "subject": ["NAME", ContractNonTerminal.SUBJECT],
            "verb_status": ["delivered", ContractNonTerminal.VERB_STATUS],
            "object": ["GBP 0", ContractNonTerminal.OBJECT],
            "date": [("on ADATE", "27 January 2002"), ContractNonTerminal.DATE],
            "modal_verb": ["shall", ContractNonTerminal.MODAL_VERB],
            "verb": ["pay", ContractNonTerminal.VERB],
            "numerical_expression": ["0", ContractNonTerminal.NUMERICAL_EXPRESSION],
            "logical_operator": ["and", ContractNonTerminal.LOGICAL_OPERATOR],
            "comparison": ["more than", ContractNonTerminal.COMPARISON],
            "other_subject": ["some thing", ContractNonTerminal.SUBJECT],
        }
        valid_types = {
            "subject verb status": [
                "holds",
                "subject",
                "verb_status",
                "object",
                "date",
            ],
            "subject date": ["holds", "subject", "date", "verb_status", "object"],
            "date subject": ["holds", "date", "subject", "verb_status", "object"],
            "subject modal verb": [
                "holds",
                "subject",
                "modal_verb",
                "verb",
                "object",
                "date",
            ],
            "boolean expression": [
                "holds",
                "subject",
                "verb_status",
                "comparison",
                "other_subject",
            ],
        }
        valid_operators = {"and", "or"}
        BaseComponent.__init__(
            self, condition_id, condition_type, valid_types, components
        )
        BaseChain.__init__(self, valid_operators, SimpleCondition)
        self._logic_operator = "and"
        self._next = None

    def get_display_text(self):
        match self.get_type():
            case "subject verb status":
                out_text = f'[{self.get_id()}] {self._get_component_value("holds")} {self._get_component_value("subject")} {self._get_component_value("verb_status")} {self._get_component_value("object")} {self._get_component_value("date")}'
            case "subject date":
                out_text = f'[{self.get_id()}] {self._get_component_value("holds")} {self._get_component_value("subject")} {self._get_component_value("date")} {self._get_component_value("verb_status")} {self._get_component_value("object")}'
            case "date subject":
                out_text = f'[{self.get_id()}] {self._get_component_value("holds")} {self._get_component_value("date")} {self._get_component_value("subject")} {self._get_component_value("verb_status")} {self._get_component_value("object")}'
            case "subject modal verb":
                out_text = f'[{self.get_id()}] {self._get_component_value("holds")} {self._get_component_value("subject")} {self._get_component_value("modal_verb")} {self._get_component_value("verb")} {self._get_component_value("object")} {self._get_component_value("date")}'
            case "boolean expression":
                out_text = f'[{self.get_id()}] {self._get_component_value("holds")} {self._get_component_value("subject")} {self._get_component_value("verb_status")} {self._get_component_value("comparison")} {self._get_component_value("other_subject")} '
            case _:
                raise ValueError(f"Invalid condition type: {self.get_type()}")
        if self._next:
            return f"{out_text} {self._logic_operator} {self._next.get_display_text()}"
        return out_text
