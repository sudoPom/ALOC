"""
BaseChain Module

This module defines the BaseChain class, representing a list of components joined
by logical operators.

Classes:
- BaseChain: Represents a list of components.

"""

from model.components.simple_component import SimpleComponent


class ChainComponent(SimpleComponent):
    def __init__(self, component_id, component_spec):
        super().__init__(component_id, component_spec)
        self.__component_spec = component_spec
        self.__next = None

    def add_next(self, id, component_type):
        old_next = self.__next
        self.__next = ChainComponent(id + 1, self.__component_spec)
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

    def get_display_text(self):
        text = super().get_display_text()
        print(text)
        if not self.__next:
            text = " ".join(text.split(" ")[:-1])
        print(text)
        return text