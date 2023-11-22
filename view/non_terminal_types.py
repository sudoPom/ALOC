from enum import Enum


class ContractNonTerminal(Enum):
    SUBJECT = "Subject"
    NUMERICAL_EXPRESSION = "Numerical Expression"

    @staticmethod
    def validate_subject(subject_string):
        return len(subject_string) > 0

    @staticmethod
    def validate_numerical_expression(numerical_expression_string):
        return numerical_expression_string.isnumeric()
