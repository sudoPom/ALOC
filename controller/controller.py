from model.model import Model


class Controller:

    def __init__(self, model):
        self.__model = model

    def get_contract(self):
        return self.__model.get_contract()

    def add_new_definition(self, definition_type):
        self.__model.add_definition(definition_type)

    @staticmethod
    def change_definition_type(definition, definition_type):
        Model.change_definition_type(definition, definition_type)

    @staticmethod
    def update_definition(definition, update_dict):
        Model.update_definition(definition, update_dict)

    def delete_definition(self, definition_id):
        self.__model.delete_definition(definition_id)
