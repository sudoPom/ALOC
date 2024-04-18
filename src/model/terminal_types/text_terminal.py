from src.model.terminal_types.terminal import Terminal, TerminalTypeNames
from src.parser.base_parser import BaseParser


class TextTerminal(Terminal):
    """
    TextTerminal class represents a terminal that can be expressed through text.


    Args:
        name (str): The name of the terminal.
        default (str): The default text for this terminal.
        parser (:obj:`BaseParser`): Parser responsible for validating textual input.
        explanation (str): The error text to show if the user enters an invalid value for this terminal.
    Note:
        The JSON representation of this class requires:
            :obj:`name` attribute of type str.
            :obj:`default` attribute of type str (This should be a valid value for this terminal.).
            :obj:`parser_root` attribute of type str (This should be a valid LHS of the :obj:`BaseParser`'s grammar.).
            :obj:`explanation` of type str.
    """

    def __init__(
        self, name: str, default: str, parser: BaseParser, explanation: str
    ) -> None:
        super().__init__(name, default, TerminalTypeNames.TEXT)
        self.__explanation = explanation
        self.__parser = parser
        assert self.__parser.parse(
            default
        ), f"The default of a text terminal must be valid. {default} is not a valid {name} terminal according to the grammar."

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
