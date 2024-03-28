from typing import List

from src.model.terminal_types.terminal import Terminal, TerminalTypeNames


class MultiChoiceTerminal(Terminal):
    EMPTY_CHOICE = "EMPTY"

    def __init__(self, name, default, choices: List, allow_empty):
        super().__init__(name, default, TerminalTypeNames.MULTI_CHOICE)
        self.__choices = choices
        if allow_empty:
            self.__choices.append(self.EMPTY_CHOICE)

    def get_choices(self):
        return self.__choices
