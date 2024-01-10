from lark import Lark, exceptions

COLA_GRAMMAR = """
    start: contract

    contract: component
        | component "C_AND" contract
    component: definition
        | conditional_definition
        | statement
        | conditional_statement
    definition: simple_definition
        | simple_definition "AND" definition
    simple_definition: id subject "IS" subject
        | id subject "EQUALS" numerical_expression
    numerical_expression: num
        | numerical_object
        | numerical_expression operator numerical_expression
    operator: plus
        | minus
        | times
        | divide
    conditional_definition: definition "IF" condition
        | "IF" condition "THEN" definition
    statement: simple_statement
        | simple_statement "OR" statement
        | simple_statement "AND" statement
    conditional_statement: statement "IF" condition
        | "IF" condition "THEN" statement
    simple_statement: id holds? subject modal_verb verb object date
        | id holds? subject date modal_verb verb object
        | id holds? date subject modal_verb verb object
    condition: simple_condition
        | simple_condition "OR" condition
        | simple_condition "AND" condition
    simple_condition: id holds? subject verb_status object date
        | id holds? subject date verb_status object
        | id holds? date subject verb_status object
        | id holds? subject modal_verb verb object date
        | id holds? boolean_expression
    boolean_expression: subject verb_status comparison subject
    id: "[" num "]"
        | "[" num "(" num ")]"
    holds: "it is the case that"
        | "it is not the case that"
    subject: string
    verb: deliver
        | pay
        | charge
    verb_status: delivered
        | paid
        | charged
    comparison: lessthan
        | equalto
        | morethan
    modal_verb: obligation
        | permission
        | prohibition
    date: "on the " num " " month " " num
        | "on ANYDATE"
        | "on ADATE"
        | "on THEDATE"
    month: "January"
        | "February"
        | "March"
        | "April"
        | "May"
        | "June"
        | "July"
        | "August"
        | "September"
        | "October"
        | "November"
        | "December"
    object: numerical_object
        | nonnumerical_object
    numerical_object: pounds " " num
        | dollars " " num
        | euros " " num
        | amount subject
    nonnumerical_object: "SOMECURRENCY " string
        | "REPORT " string
        | "NAMEDOBJECT " string
        | "OTHEROBJECT " string
    string: char
        | char string
    char: "a".."z"
        | "A".."Z"
        | " "
    num: digit
        | digit num
    digit: "0".."9"
    deliver: "deliver"
    pay: "pay"
    charge: "charge"
    delivered: "delivered"
    paid: "paid"
    charged: "charged"
    lessthan: "less than"
    equalto: "equals"
        | "equal to"
    morethan: "more than"
        | "greater than"
    obligation: "shall"
        | "must"
    permission: "may"
    prohibition: "is forbidden to"
    pounds: "GBP"
        | "pounds"
        | "quid"
    dollars: "USD"
        | "dollars"
        | "bucks"
    euros: "EUR"
        | "euros"
    plus: "+"
        | "PLUS"
    minus: "-"
        | "MINUS"
    times: "*"
        | "TIMES"
    divide: "/"
        | "DIVIDE"
    amount: "AMOUNT"
"""


class BaseParser:
    def __init__(self, start_from: str):
        self.__parser = Lark(COLA_GRAMMAR, start=start_from)

    def parse(self, input_string: str):
        try:
            self.__parser.parse(input_string)
            return True
        except exceptions.LarkError as e:
            print(e)
            return False
