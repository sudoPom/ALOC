"""
BaseChain Module

This module defines the BaseChain class, representing a list of components joined
by logical operators.

Classes:
- BaseChain: Represents a list of components.

"""


class BaseChain:

    def __init__(self, valid_operators, chain_type):
        self._valid_operators = valid_operators
        self._next = None
        self._chain_type = chain_type

    def add_next(self):
        old_next = self._next
        self._next = self._chain_type(
            self.get_id() + 1, self.get_type())
        self._next.set_next(old_next)

    def set_next(self, next):
        self._next = next

    def delete_next_condition(self):
        if not self._next:
            return
        self._next = self._next.get_next_component()

    def get_next_component(self):
        return self._next

    def set_logic_operator(self, operator):
        if operator not in {"and", "or"}:
            raise ValueError(f"Invalid operator: {operator}")
        self._logic_operator = operator
