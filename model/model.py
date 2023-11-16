from model.contract import Contract


class Model():

    def __init__(self):
        self.__contract = Contract()
        self.__contract.add_definition("subject pair")
        self.__contract.add_definition("subject pair")
        self.__contract.add_definition("subject pair")
        self.__contract.add_definition("subject pair")

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
