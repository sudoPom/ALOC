class Controller:

    def __init__(self, model):
        self.__model = model

    def get_contract(self):
        return self.__model.get_contract()
