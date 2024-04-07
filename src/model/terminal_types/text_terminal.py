from src.model.terminal_types.terminal import Terminal, TerminalTypeNames
from src.parsers.base_parser import BaseParser


class TextTerminal(Terminal):
    """
    TextTerminal class represents a terminal that can be expressed through text.


    Args:
        name (str): The name of the terminal.
        default (str): The default text for this terminal.
        parse_string (str): Where in the :obj:`BaseParser` grammar to verify this terminal.
        explanation (str): The error text to show if the user enters an invalid value for this terminal.
    """

    def __init__(
        self, name: str, default: str, parse_root: str, explanation: str
    ) -> None:
        super().__init__(name, default, TerminalTypeNames.TEXT)
        self.__parse_root = parse_root
        self.__explanation = explanation
        self.__parser = BaseParser(self.__parse_root)

    def get_parse_root(self):
        """
        Returns the parser root for validating this terminal.

        Returns:
            str: The parser root for validating this terminal.
        """
        return self.__parse_root

    def get_explanation(self):
        """
        Returns the error explanation for this terminal.

        Returns:
            The error explanation for this terminal.
        """
        return self.__explanation

    def get_parser(self):
        """
        Returns the parser associated with this terminal.

        Returns:
            :obj:`BaseParser`: The parser associated with this terminal.
        """
        return self.__parser

    def validate(self, text: str):
        """
        Returns whether the value passes in is of this terminal type.

        Args:
            value (str): The value to check.

        Returns:
            bool: True if the value is an instance of this terminal, False otherwise.
        """
        return self.__parser.parse(text)
