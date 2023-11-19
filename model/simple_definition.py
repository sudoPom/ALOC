from model.utils import extract_key, throw_if_no_keys_found


class SimpleDefinition:
    def __init__(self, id, type):
        self.__type = type
        self.__id = id
        self.__subject = "SUBJECT"
        self.__other_subject = "OTHER SUBJECT"
        self.__numerical_expression = "NUMERICAL EXPRESSION"
        self.__components = {"subject",
                             "other_subject", "numerical_expression"}
        self.__types = {"subject pair", "subject numerical pair"}

    def update(self, **kwargs):
        throw_if_no_keys_found(kwargs, self.__components)
        self.__subject = extract_key(kwargs, "subject". self.__subject)
        self.__other_subject = extract_key(
            kwargs, "other_subject". self.__other_subject)
        self.__numerical_expression = extract_key(
            kwargs, "numerical_expression", self.__numerical_expression)

    def set_type(self, type):
        if type not in self.__types:
            raise ValueError(f"Invalid definition type, {type}")
        self.__type = type

    def get_type(self):
        return self.__type

    def get_id(self):
        return self.__id

    def get_subject(self):
        return self.__subject

    def get_other_subject(self):
        return self.__other_subject

    def get_numerical_expression(self):
        return self.__numerical_expression
