import uuid

from model.simple_definition import (NumericalSimpleDefinition,
                                     SubjectSimpleDefinition)


class Contract:

    def __init__(self):
        self.definitions = []


    def add_new_definition(self, definition_type):
        match definition_type:
            case "subject":
                self.definitions.append(SubjectSimpleDefinition())
            case "numerical":
                self.definitions.append(NumericalSimpleDefinition())
            case _:
                raise ValueError(f"Invalid definition type {definition_type}")

    def update_definition(self, id, **kwargs):
        for definition in definitions:
            if definition.get_id() == id:
                definition.update(kwargs)
                return
        raise ValueError(f"This definition does not exist! {id}")
