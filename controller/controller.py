"""
Controller Module

This module defines the Controller class, which serves as the controller in
the MVC architecture.

Classes:
- Controller: The controller in the MVC architecture.

"""

from model.component_attribute import ComponentAttribute
from model.component_specifications.conditional_component_spec import ConditionalComponentSpec
from model.model import Model
from model.component_specifications.simple_component_spec import SimpleComponentSpec
from model.type_spec import TypeSpec
from view.terminal_types import Terminal


class Controller:
    """
    Controller serves as the controller in the MVC architecture.

    Methods:
    - __init__(model): Initializes a Controller object.
    - get_contract(): Retrieves the current contract from the model.
    - add_new_definition(definition_type): Adds a new definition to the
    contract through the model.
    - change_definition_type(definition, definition_type): Changes the type of
    a definition through the model.
    - update_definition(definition, update_dict): Updates a definition through
    the model.
    - delete_definition(definition_id): Deletes a definition from the contract
    through the model.
    - add_new_statement(statement_type): Adds a new statement to the contract
    through the model.
    - change_statement_type(statement, statement_type): Changes the type of a
    statement through the model.
    - update_statement(statement, update_dict): Updates a statement through
    the model.
    - delete_statement(statement_id): Deletes a statement from the contract
    through the model.

    """

    def __init__(self, model: Model):
        """
        Initializes a Controller object.

        Args:
        - model (Model): The model instance to be associated with the
        controller.
        """
        self.__model = model
        definition_spec = SimpleComponentSpec(
            "definition",
            [
                TypeSpec(
                    "subject pair",
                    "[{}] {} IS {} {}",
                    ["subject", "other_subject", "logical_operator"],
                    "Subject-Pair Definition",
                ),
                TypeSpec(
                    "subject numerical pair",
                    "[{}] {} EQUALS {} {}",
                    ["subject", "numerical_expression", "logical_operator"],
                    "Numerical Definition",
                ),
            ],
            [
                ComponentAttribute("subject", Terminal.SUBJECT),
                ComponentAttribute("other_subject", Terminal.SUBJECT),
                ComponentAttribute(
                    "numerical_expression", Terminal.NUMERICAL_EXPRESSION
                ),
                ComponentAttribute("logical_operator", Terminal.LOGICAL_AND),
            ],
            "definitions",
            "base_chain",
        )
        statement_spec = SimpleComponentSpec(
            "statement",
            [
                TypeSpec(
                    "subject modal",
                    "[{}] {} {} {} {} {} {} {}",
                    [
                        "holds",
                        "subject",
                        "modal_verb",
                        "verb",
                        "object",
                        "date",
                        "logical_operator",
                    ],
                    "Subject-Modal Statement",
                ),
                TypeSpec(
                    "subject date",
                    "[{}] {} {} {} {} {} {}",
                    [
                        "holds",
                        "subject",
                        "modal_verb",
                        "verb",
                        "object",
                        "date",
                        "logical_operator",
                    ],
                    "Subject-Date Statement",
                ),
                TypeSpec(
                    "date subject",
                    "[{}] {} {} {} {} {} {}",
                    [
                        "holds",
                        "subject",
                        "modal_verb",
                        "verb",
                        "object",
                        "date",
                        "logical_operator",
                    ],
                    "Date-Subject Statement",
                ),
            ],
            [
                ComponentAttribute("holds", Terminal.HOLDS),
                ComponentAttribute("subject", Terminal.SUBJECT),
                ComponentAttribute("modal_verb", Terminal.MODAL_VERB),
                ComponentAttribute("verb", Terminal.VERB),
                ComponentAttribute("object", Terminal.OBJECT),
                ComponentAttribute("date", Terminal.DATE),
                ComponentAttribute(
                    "logical_operator", Terminal.LOGICAL_OPERATOR
                ),
            ],
            "other_components",
            "base_chain",
        )

        condition_spec = SimpleComponentSpec(
            "condition",
            [
                TypeSpec(
                    "subject verb_status",
                    "[{}] {} {} {} {} {} {}",
                    [
                        "holds",
                        "subject",
                        "verb_status",
                        "object",
                        "date",
                        "logical_operator",
                    ],
                    "Subject-Verb-Status Condition",
                ),
                TypeSpec(
                    "subject verb_status",
                    "[{}] {} {} {} {} {} {}",
                    [
                        "holds",
                        "subject",
                        "date",
                        "verb_status",
                        "object",
                        "logical_operator",
                    ],
                    "Subject-Date Condition",
                ),
                TypeSpec(
                    "subject verb_status",
                    "[{}] {} {} {} {} {} {}",
                    [
                        "holds",
                        "date",
                        "subject",
                        "verb_status",
                        "object",
                        "logical_operator",
                    ],
                    "Date-Subject Condition",
                ),
                TypeSpec(
                    "subject verb_status",
                    "[{}] {} {} {} {} {} {}",
                    [
                        "holds",
                        "subject",
                        "modal_verb",
                        "verb," "object",
                        "date",
                        "logical_operator",
                    ],
                    "Subject-Modal-Verb Condition",
                ),
                TypeSpec(
                    "subject verb_status",
                    "[{}] {} {} {} {} {} {}",
                    [
                        "holds",
                        "subject",
                        "verb_status",
                        "comparison",
                        "other_subject",
                        "logical_operator",
                    ],
                    "Boolean-Expression Condition",
                ),
            ],
            [
                ComponentAttribute("holds", Terminal.HOLDS),
                ComponentAttribute("subject", Terminal.SUBJECT),
                ComponentAttribute("verb_status", Terminal.VERB_STATUS),
                ComponentAttribute("object", Terminal.OBJECT),
                ComponentAttribute("date", Terminal.DATE),
                ComponentAttribute("modal_verb", Terminal.MODAL_VERB),
                ComponentAttribute("comparison", Terminal.COMPARISON),
                ComponentAttribute("other_subject", Terminal.SUBJECT),
                ComponentAttribute(
                    "logical_operator", Terminal.LOGICAL_OPERATOR
                ),
            ],
            "nowhere",
            "base_chain",
        )

        self.__component_dict = {
            "definition": definition_spec,
            "statement": statement_spec,
            "conditional_definition": ConditionalComponentSpec(
                "conditional_definition",
                [
                    TypeSpec("if", "", "", "If Conditional"),
                    TypeSpec("if then", "", "", "If-Then Conditional"),
                ],
                "other_components",
                "conditional",
                condition_spec,
                definition_spec,
            ),
            "conditional_statement": ConditionalComponentSpec(
                "conditional_statement",
                [
                    TypeSpec("if", "", "", "If Conditional"),
                    TypeSpec("if then", "", "", "If-Then Conditional"),
                ],
                "other_components",
                "conditional",
                condition_spec,
                statement_spec,
            ),
        }

    def get_contract_path(self):
        return self.__model.get_contract().get_path()

    def save_contract(self, path):
        self.__model.save_contract_file(path)

    def load_contract(self, path):
        self.__model.open_contract_file(path)

    def create_new_contract(self):
        self.__model.create_new_contract()

    def get_contract(self):
        """
        Retrieves the current contract from the model.

        Returns:
        - Contract: The current contract.
        """
        return self.__model.get_contract()

    def add_new_component(self, component):
        component_spec = self.__component_dict[component]
        self.__model.add_component(component_spec)

    def delete_component(self, component_id):
        self.__model.delete_component(component_id)

    @staticmethod
    def change_component_type(component, component_type):
        """
        Changes the type of a definition through the model.

        Args:
        - definition: The definition whose type will be changed.
        - definition_type: The new type of the definition.
        """
        Model.change_component_type(component, component_type)

    @staticmethod
    def update_component(component, update_dict):
        """
        Updates a definition through the model.

        Args:
        - definition: The definition to be updated.
        - update_dict: The key-value pairs of the new definition.
        """
        Model.update_component(component, update_dict)

    def add_new_statement(self, statement_type):
        """
        Adds a new statement to the contract through the model.

        Args:
        - statement_type: The type of the new statement.
        """
        self.__model.add_statement(statement_type)

    def add_new_conditional_statement(self, conditional_statement_type):
        """
        Adds a new conditional statement to the contract through the model.

        Args:
        - conditional_statement_type: The type of the new conditional statement.
        """
        self.__model.add_conditional_statement(conditional_statement_type)

    def add_new_conditional_definition(self, conditional_definition_type):
        """
        Adds a new conditional statement to the contract through the model.

        Args:
        - conditional_statement_type: The type of the new conditional statement.
        """
        self.__model.add_conditional_definition(conditional_definition_type)

    @staticmethod
    def extend_component_chain(component):
        component.add_next(component.get_id(), component.get_type())

    def set_logic_operator(self, component, operator):
        component.set_logic_operator(operator)

    @staticmethod
    def delete_next_component_from_chain(component):
        component.delete_next_component()
