"""
ContractNonTerminal Enum

This enum represents the non-terminal symbols in a contract and provides
validation and options for each.

Enums:
- SUBJECT: Represents the Subject non-terminal.
- NUMERICAL_EXPRESSION: Represents the Numerical Expression non-terminal.
- DATE: Represents the Date non-terminal.
- VERB: Represents the Verb non-terminal.
- MODAL_VERB: Represents the Modal Verb non-terminal.
- OBJECT: Represents the Object non-terminal.
- HOLDS: Represents the Holds non-terminal.

Methods:
- validate_subject(subject): Validates a Subject entry.
- validate_numerical_expression(numerical_expression): Validates a Numerical
Expression entry.
- validate_modal_verb(modal_verb): Validates a Modal Verb entry.
- validate_verb(verb): Validates a Verb entry.
- validate_date(date): Validates a Date entry.
- validate_object(object): Validates an Object entry.
- validate_holds(holds): Validates a Holds entry.
- validate_entry(entry, entry_type): Validates an entry based on its type.
- get_options(entry_type): Retrieves options for a given entry type.

"""

from enum import Enum

from parsers.base_parser import BaseParser


class Terminal(Enum):
    SUBJECT = "SUBJECT"
    NUMERICAL_EXPRESSION = "0"
    DATE = ("on ADATE", "27 January 2002")
    VERB = "pay"
    VERB_STATUS = "paid"
    MODAL_VERB = "shall"
    OBJECT = "GBP 0"
    HOLDS = "it is the case that"
    COMPARISON = "equal to"
    LOGICAL_OPERATOR = "or"
    LOGICAL_AND = "and"

    @staticmethod
    def validate_subject(subject):
        """
        Validates a Subject entry.

        Args:
        - subject (str): The Subject entry.

        Returns:
        - bool: True if the entry is valid, False otherwise.
        """
        return BaseParser("subject").parse(subject)

    @staticmethod
    def validate_numerical_expression(numerical_expression):
        """
        Validates a Numerical Expression entry.

        Args:
        - numerical_expression (str): The Numerical Expression entry.

        Returns:
        - bool: True if the entry is valid, False otherwise.
        """
        return BaseParser("numerical_expression").parse(numerical_expression)

    @staticmethod
    def validate_date(date):
        """
        Validates a Date entry.

        Args:
        - date (str): The Date entry.

        Returns:
        - bool: True if the entry is valid, False otherwise.
        """
        print(date)
        if date in Terminal.get_options(Terminal.DATE):
            return True
        return BaseParser("date").parse(f"on the {date}")

    @staticmethod
    def validate_object(object):
        """
        Validates an Object entry.

        Args:
        - object (str): The Object entry.

        Returns:
        - bool: True if the entry is valid, False otherwise.
        """
        return BaseParser("object").parse(object)

    @staticmethod
    def validate_holds(holds):
        """
        Validates a Holds entry.

        Args:
        - holds (str): The Holds entry.

        Returns:
        - bool: True if the entry is valid, False otherwise.
        """
        return BaseParser("holds").parse(holds)

    @classmethod
    def is_optional(cls, entry_type):
        return entry_type in {
            cls.HOLDS,
            cls.VERB,
            cls.VERB_STATUS,
            cls.MODAL_VERB,
            cls.DATE,
            cls.LOGICAL_OPERATOR,
            cls.COMPARISON,
            cls.LOGICAL_AND,
        }

    @classmethod
    def validate_entry(cls, entry, entry_type):
        """
        Validates an entry based on its type.

        Args:
        - entry (str): The entry to be validated.
        - entry_type (ContractNonTerminal): The type of the entry.

        Returns:
        - bool: True if the entry is valid, False otherwise.

        Raises:
        - ValueError: If the entry_type is not supported.
        """
        if cls.is_optional(entry_type) and entry_type is not cls.DATE:
            return True
        match entry_type:
            case cls.SUBJECT:
                return cls.validate_subject(entry)
            case cls.NUMERICAL_EXPRESSION:
                return cls.validate_numerical_expression(entry)
            case cls.DATE:
                return cls.validate_date(entry)
            case cls.OBJECT:
                return cls.validate_object(entry)
            case cls.HOLDS:
                return cls.validate_holds(entry)
            case _:
                raise ValueError(f"Invalid entry type: {entry_type}")

    @classmethod
    def get_options(cls, entry_type):
        """
        Retrieves options for a given entry type.

        Args:
        - entry_type (ContractNonTerminal): The type of the entry.

        Returns:
        - list: A list of options for the entry_type.

        Raises:
        - ValueError: If the entry_type does not support option entry.
        """
        match entry_type:
            case cls.HOLDS:
                return ["it is the case that ", "it is not the case that ", ""]
            case cls.VERB:
                return ["deliver", "pay", "charge"]
            case cls.MODAL_VERB:
                return ["shall", "must", "may", "is forbidden to"]
            case cls.DATE:
                return ["on ADATE", "on THEDATE", "on ANYDATE", "custom date"]
            case cls.LOGICAL_OPERATOR:
                return ["and", "or"]
            case cls.LOGICAL_AND:
                return ["and"]
            case cls.COMPARISON:
                return ["less than", "equal to", "more than"]
            case cls.VERB_STATUS:
                return ["delivered", "paid", "charged"]
            case _:
                raise ValueError(f"Type '{entry_type}' does not support option entry.")

    @classmethod
    def error_explanation(cls, entry_type):
        match entry_type:
            case cls.DATE:
                return "Custom dates must be of the form:\nnumber month number"
            case cls.OBJECT:
                return 'Objects must be of the form: GBP/USD/SOMECURRENCY number or\nREPORT/SOMECURRENCY/NAMEDOBJECT/OTHEROBJECT "text"'
            case cls.NUMERICAL_EXPRESSION:
                return "Numerical expressions must be of the form:\n'number OPERATOR number OPERATOR number...'\nOPERATOR can be either:\nPLUS, MINUS, TIMES or DIVIDE"
            case cls.SUBJECT:
                return "Subjects must only contain non numerical characters and spaces."
            case _:
                raise ValueError(f"No error provided for entry type:{entry_type}")

    @classmethod
    def from_string(cls, string):
        match string:
            case "subject":
                return cls.SUBJECT
            case "numerical_expression":
                return cls.NUMERICAL_EXPRESSION
            case "date":
                return cls.DATE
            case "object":
                return cls.OBJECT
            case "logical_and":
                return cls.LOGICAL_AND
            case "logical_operator":
                return cls.LOGICAL_OPERATOR
            case "verb":
                return cls.VERB
            case "modal_verb":
                return cls.MODAL_VERB
            case "verb_status":
                return cls.VERB_STATUS
            case "holds":
                return cls.HOLDS
            case "comparison":
                return cls.COMPARISON
            case _:
                raise ValueError(f"Invalid terminal type {string}")
