from src.model.terminal_types.terminal import Terminal, TerminalTypeNames
from src.parsers.base_parser import BaseParser


class TextTerminal(Terminal):
    def __init__(self, name, default, parse_root, explanation) -> None:
        super().__init__(name, default, TerminalTypeNames.TEXT)
        self.__parse_root = parse_root
        self.__explanation = explanation
        self.__parser = BaseParser(self.__parse_root)

    def get_parse_root(self):
        return self.__parse_root

    def get_explanation(self):
        return self.__explanation

    def get_parser(self):
        return self.__parser

    def validate(self, text: str):
        return self.__parser.parse(text)
