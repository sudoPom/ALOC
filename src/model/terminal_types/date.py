from model.attribute_types.attribute import Attribute, AttributeTypeNames
from model.attribute_types.multi_choice_attribute import MultiChoiceAttribute
from model.attribute_types.text_attribute import TextAttribute


class Date(TextAttribute, MultiChoiceAttribute):
    def __init__(
        self, name, default_option, default_date, parse_string, explanation, choices
    ):
        TextAttribute.__init__(self, name, default_date, parse_string, explanation)
        MultiChoiceAttribute.__init__(self, name, default_option, choices)
