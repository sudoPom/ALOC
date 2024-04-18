from typing import List

from src.model.terminal_types.terminal import Terminal, TerminalTypeNames
from src.parser.base_parser import BaseParser


class HybridTerminal(Terminal):
    """
    HybridTerminal class represents a terminal that can either be expressed through text or through a multiple choice selection.


    Args:
        name (str): The name of the terminal.
        default_option (str): The default multiple choice option selected for this terminal.
        default_text (str): The default text for this terminal.
        parser (:obj:`BaseParser`): Parser responsible for validating textual input.
        explanation (str): The error text to show if the user enters an invalid value for this terminal.
        choices (:obj:`List[str]`): The possible choices the user can select from for this terminal.
    Note:
        The JSON representation of this class requires:
            :obj:`name` attribute of type str.
            :obj:`default_text` attribute of type str (This should be a valid value for this terminal.).
            :obj:`default_option` attribute of type str (This should be in the choices list.).
            :obj:`choices` attribute of type :obj:`List[str]`.
            :obj:`explanation` of type str.
    """

    CUSTOM_OPTION = "CUSTOM"

    def __init__(
        self,
        name: str,
        default_option: str,
        default_text: str,
        parser: BaseParser,
        explanation: str,
        choices: List[str],
    ):
        super().__init__(name, (default_option, default_text), TerminalTypeNames.HYBRID)
        self.__explanation = explanation
        self.__choices = choices
        self.__choices.append(self.CUSTOM_OPTION)
        self.__parser = parser

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
