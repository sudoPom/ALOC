from src.model.terminal_types.terminal import Terminal, TerminalTypeNames
from src.parsers.base_parser import BaseParser


class HybridTerminal(Terminal):
    def __init__(
        self, name, default_option, default_text, parse_string, explanation, choices
    ):
        super().__init__(name, (default_option, default_text), TerminalTypeNames.HYBRID)
        self.__parse_root = parse_string
        self.__explanation = explanation
        self.__choices = choices
        self.__parser = BaseParser(self.__parse_root)

    def get_parse_root(self):
        return self.__parse_root

    def get_explanation(self):
        return self.__explanation

    def validate(self, value: str):
        if value in self.get_choices():
            return True
        return self.__parser.parse(f"on the {value}")

    def get_choices(self):
        return self.__choices
