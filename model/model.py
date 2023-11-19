from model.contract import Contract


class Model():

    def __init__(self):
        self.__contract = Contract()

    def add_definition(self, definition_type):
        self.__contract.add_definition(definition_type)

    def change_definition_type(self, definition, definition_type):
        definition.set_type(definition_type)

    def get_contract(self):
        """Returns the current contract.

        Returns:
            The contract currently being drafted.
        """
        return self.__contract

    def save_contract_file(path: str):
        """Saves the current contract.

        Args:
            path: The file path of where the contract should be saved.
        """
        pass

    def open_contract_file(path: str):
        """Loads the contract stored in the file pointed to by path.

        Args:
            path: The file path to retrieve the contract from.
        """
        pass
