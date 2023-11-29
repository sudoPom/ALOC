"""
SimpleStatement Module

This module defines the SimpleStatement class, representing a simple statement
in the AST.

Classes:
- SimpleStatement: Represents a simple statement in the AST.

"""

from model.base_component import BaseComponent
from view.non_terminal_types import ContractNonTerminal


class SimpleStatement(BaseComponent):
    """
    Represents a simple statement in the AST.

    Methods:
    - __init__(id, statement_type): Initialize a SimpleStatement object.
    - update(**kwargs): Update the attributes of the simple statement.
    - get_components(): Get a dictionary of components in the simple statement.
    - get_subject(): Get the subject of the simple statement.
    - get_object(): Get the object of the simple statement.
    - get_holds(): Get the "holds" component of the simple statement.
    - get_modal_verb(): Get the modal verb of the simple statement.
    - get_verb(): Get the verb of the simple statement.
    - get_date(): Get the date of the simple statement.

    """

    def __init__(self, statement_id, statement_type):
        """
        Initialize a SimpleStatement object.

        Args:
        - id (str): The ID of the simple statement.
        - statement_type (str): The type of the simple statement.
        """
        components = {
            "holds": ["it is the case that", ContractNonTerminal.HOLDS],
            "subject": ["NAME", ContractNonTerminal.SUBJECT],
            "modal_verb": ["shall", ContractNonTerminal.MODAL_VERB],
            "verb": ["pay", ContractNonTerminal.VERB],
            "object": ["$0", ContractNonTerminal.OBJECT],
            "date": [("on a date", "on the 27 January 2002"), ContractNonTerminal.DATE],
        }
        valid_types = {
            "subject modal": components.keys(),
            "subject date": components.keys(),
            "date subject": components.keys()
        }
        super().__init__(
            statement_id,
            statement_type,
            valid_types,
            components
        )

    def get_display_text(self):
        match self.get_type():
            case "subject modal":
                return f"{self._get_component_value('holds')} {self._get_component_value('subject')} {self._get_component_value('modal_verb')} {self._get_component_value('verb')} {self._get_component_value('object')} {self._get_component_date('date')}"
            case "subject date":
                return f"{self._get_component_value('holds')} {self._get_component_value('subject')} {self._get_component_date('date')} {self._get_component_value('modal_verb')} {self._get_component_value('verb')} {self._get_component_value('object')}"
            case "date subject":
                return f"{self._get_component_value('holds')} {self._get_component_date('date')} {self._get_component_value('subject')} {self._get_component_value('modal_verb')} {self._get_component_value('verb')} {self._get_component_value('object')}"
            case _:
                raise ValueError("Invalid statement type: {self.__type}")
