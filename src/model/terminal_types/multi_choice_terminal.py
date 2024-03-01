from typing import List

from src.model.terminal_types.terminal import Terminal, TerminalTypeNames


class MultiChoiceTerminal(Terminal):
    def __init__(self, name, default, choices: List):
        super().__init__(name, default, TerminalTypeNames.MULTI_CHOICE)
        self.__choices = choices
        print(self.__choices)

    def get_choices(self):
        return self.__choices
