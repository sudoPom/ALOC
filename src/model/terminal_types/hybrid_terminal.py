from src.model.terminal_types.terminal import Terminal, TerminalTypeNames
from src.parsers.base_parser import BaseParser


class HybridTerminal(Terminal):
    """
    HybridTerminal class represents a terminal that can either be expressed through text or through a multiple choice selection.


    Args:
        name (str): The name of the terminal.
        default_option (str): The default multiple choice option selected for this terminal.
        default_text (str): The default text for this terminal.
        parse_string (str): Where in the :obj:`BaseParser` grammar to verify this terminal.
        explanation (str): The error text to show if the user enters an invalid value for this terminal.
        choices (:obj:`List[str]`): The possible choices the user can select from for this terminal.
    """

    CUSTOM_OPTION = "CUSTOM"

    def __init__(
        self, name, default_option, default_text, parse_string, explanation, choices
    ):
        super().__init__(name, (default_option, default_text), TerminalTypeNames.HYBRID)
        self.__parse_root = parse_string
        self.__explanation = explanation
        self.__choices = choices
        self.__choices.append(self.CUSTOM_OPTION)
        self.__parser = BaseParser(self.__parse_root)

    def get_parse_root(self) -> str:
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

    def validate(self, value: str) -> bool:
        """
        Returns whether the value passes in is of this terminal type.

        Args:
            value (str): The value to check.

        Returns:
            bool: True if the value is an instance of this terminal, False otherwise.
        """
        if value in self.get_choices():
            return True
        return self.__parser.parse(f"on the {value}")

    def get_choices(self):
        """
        Returns the possible choices that satisfy this terminal.

        Returns:
            :obj:`List[str]`: The possible choices that satisft this terminal.
        """
        return self.__choices
