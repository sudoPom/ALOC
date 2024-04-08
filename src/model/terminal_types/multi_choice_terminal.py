from typing import List

from src.model.terminal_types.terminal import Terminal, TerminalTypeNames


class MultiChoiceTerminal(Terminal):
    """
    MultiChoiceTerminal class represents a terminal that has a reasonable amount of choices to select from.


    Args:
        name (str): The name of the terminal.
        default (str): The default multiple choice option selected for this terminal.
        choices (:obj:`List[str]`): The possible choices the user can select from for this terminal.
        allow_empty (bool): Whether or not the empty string is a valid option.
    Note:
        The JSON representation of this class requires:
            :obj:`name` attribute of type str.
            :obj:`default` attribute of type str (This should be a valid value for this terminal.).
            :obj:`choices` attribute of type :obj:`List[str]`.
        and Optionally:
            :obj:`allow_empty` attribute of type bool.
    """

    EMPTY_CHOICE = "EMPTY"

    def __init__(self, name, default, choices: List, allow_empty: bool):
        super().__init__(name, default, TerminalTypeNames.MULTI_CHOICE)
        self.__choices = choices
        if allow_empty:
            self.__choices.append(self.EMPTY_CHOICE)

    def get_choices(self):
        """
        Returns the possible choices that satisfy this terminal.

        Returns:
            :obj:`List[str]`: The possible choices that satisft this terminal.
        """
        return self.__choices
