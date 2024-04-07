from enum import Enum


class Terminal:
    def __init__(self, name, default, terminal_type):
        self.__name = name
        self.__default = default
        self.__type = terminal_type.value

    def get_name(self):
        """
        Returns the name of this terminal.

        Returns:
            str: The name of this terminal.
        """
        return self.__name

    def get_default(self):
        """
        Returns the default of this terminal.

        Returns:
            str: The default of this terminal.
        """
        return self.__default

    def get_type(self):
        """
        Returns the type name of this terminal.

        Returns:
            str: The type name of this terminal.
        """
        return TerminalTypeNames(self.__type)

    def set_type(self, terminal_type: "TerminalTypeNames"):
        """
        Sets the type name of this terminal.

        Args:
            terminal_type (str): The name of the type of terminal to set.
        """
        self.__type = terminal_type.value


class TerminalTypeNames(Enum):
    TEXT = "text"
    MULTI_CHOICE = "multi-choice"
    HYBRID = "hybrid"
