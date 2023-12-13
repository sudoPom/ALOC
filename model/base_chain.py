"""
BaseChain Module

This module defines the BaseChain class, representing a list of components joined
by logical operators.

Classes:
- BaseChain: Represents a list of components.

"""


class BaseChain:
    def __init__(self, valid_operators, chain_type):
        self.__valid_operators = valid_operators
        self.__next = None
        self.__chain_type = chain_type

    def add_next(self, id, component_type):
        old_next = self.__next
        self.__next = self.__chain_type(id + 1, component_type)
        self.__next.set_next(old_next)

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next

    def delete_next_condition(self):
        if not self.__next:
            return
        self.__next = self.__next.get__next_component()

    def get_next_component(self):
        return self.__next

    def set_logic_operator(self, operator):
        if operator not in self.__valid_operators:
            raise ValueError(f"Invalid operator: {operator}")
        self._logic_operator = operator
