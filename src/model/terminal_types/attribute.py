from enum import Enum


class Attribute:
    def __init__(self, name, default, attribute_type):
        self.__name = name
        self.__default = default
        self.__type = attribute_type

    def get_name(self):
        return self.__name

    def get_default(self):
        return self.__default

    def get_attribute_type(self):
        return self.__type


class AttributeTypeNames(Enum):
    TEXT = "text"
    MULTI_CHOICE = "multi-choice"
    DATE = "date"
