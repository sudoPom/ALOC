from enum import Enum


class Terminal:
    def __init__(self, name, default, terminal_type):
        self.__name = name
        self.__default = default
        self.__type = terminal_type.value

    def get_name(self):
        return self.__name

    def get_default(self):
        return self.__default

    def get_type(self):
        return TerminalTypeNames(self.__type)

    def set_type(self, terminal_type: "TerminalTypeNames"):
        self.__type = terminal_type.value


class TerminalTypeNames(Enum):
    TEXT = "text"
    MULTI_CHOICE = "multi-choice"
    HYBRID = "hybrid"
