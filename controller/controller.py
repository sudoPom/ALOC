class Controller:

    def __init__(self, model):
        self.__model = model

    def get_contract(self):
        return self.__model.get_contract()

    def add_new_definition(self, definition_type):
        self.__model.add_definition(definition_type)

    def change_definition_type(self, definition, definition_type):
        self.__model.change_definition_type(definition, definition_type)
