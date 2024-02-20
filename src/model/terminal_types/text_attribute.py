from model.attribute_types.attribute import Attribute, AttributeTypeNames
from parsers.base_parser import BaseParser


class TextAttribute(Attribute):
    def __init__(self, name, default, parse_root, explanation) -> None:
        super().__init__(name, default, AttributeTypeNames.TEXT)
        self.__parse_root = parse_root
        self.__explanation = explanation
        self.__parser = BaseParser(self.__parse_root)

    def get_parse_root(self):
        return self.__parse_root

    def get_explanation(self):
        return self.__explanation

    def validate(self, text: str):
        return self.__parser.parse(text)
