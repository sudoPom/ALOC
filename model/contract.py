import uuid

from model.simple_definition import SimpleDefinition


class Contract:

    def __init__(self):
        self.__definitions = []

    def add_definition(self, definition_type):
        new_definition = SimpleDefinition(uuid.uuid4(), definition_type)
        self.__definitions.append(new_definition)

    def get_definitions(self):
        return self.__definitions

    def update_definition(self, id, **kwargs):
        for definition in definitions:
            if definition.get_id() == id:
                definition.update(kwargs)
                return
        raise ValueError(f"This definition does not exist! {id}")

    def delete_definition(self, id):
        self.__definitions = [
            definition for definition in self.__definitions if definition.get_id() != id]
