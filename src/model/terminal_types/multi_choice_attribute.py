from model.attribute_types.attribute import Attribute, AttributeTypeNames


class MultiChoiceAttribute(Attribute):
    def __init__(self, name, default, choices):
        super().__init__(name, default, AttributeTypeNames.MULTI_CHOICE)
        self.__choices = choices

    def get_choices(self):
        return self.__choices
