from lark import Lark, exceptions

with open("./src/grammar.txt") as file:
    COLA_GRAMMAR = file.read()


class BaseParser:
    def __init__(self, start_from: str, grammar: str):
        self.__start_from = start_from
        self.__grammar = grammar

    def parse(self, input_string: str):
        parser = Lark(self.__grammar, start=self.__start_from)
        try:
            parser.parse(input_string)
            return True
        except exceptions.LarkError as e:
            print(e)
            return False
