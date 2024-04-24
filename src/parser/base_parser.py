from lark import Lark, exceptions


class BaseParser:
    def __init__(self, start_from: str, grammar: str):
        self.__start_from = start_from
        self.__grammar = grammar
        print(grammar)

    def parse(self, input_string: str):
        parser = Lark(self.__grammar, start=self.__start_from)
        try:
            parser.parse(input_string)
            return True
        except exceptions.LarkError:
            return False
