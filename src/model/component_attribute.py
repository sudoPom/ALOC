from typing import Tuple

from src.model.terminal_types.terminal import Terminal


class ComponentAttribute:
    """
    Represents an attribute of a component.

    Methods:
    - __init__(name, attribute_type): Initializes a ComponentAttribute object.
    - get_name(): Retrieves the name of the attribute.
    - get_type(): Retrieves the type of the attribute.
    - get_value(): Retrieves the value of the attribute.
    - set_value(value): Sets the value of the attribute.
    - from_json(json): Constructs a ComponentAttribute object from JSON data.
    """

    def __init__(self, name: str, terminal: Terminal, prefix: str = "") -> None:
        """
        Initializes a ComponentAttribute object.

        Args:
        - name (str): The name of the attribute.
        - attribute_type (Terminal): The type of the attribute.
        """
        self.__name: str = name
        self.__terminal: Terminal = terminal
        self.__value: str | Tuple = terminal.get_default()
        self.__prefix = prefix

    def get_name(self) -> str:
        """Retrieves the name of the attribute."""
        return self.__name

    def get_terminal(self) -> Terminal:
        """Retrieves the type of the attribute."""
        return self.__terminal

    def get_value(self) -> str | Tuple:
        """Retrieves the value of the attribute."""
        if type(self.__value) == str:
            return f"{self.__prefix}{self.__value}"
        print(self.__value[0])
        return (self.__value[0], f"{self.__prefix}{self.__value[1]}")

    def create_blank(self):
        return ComponentAttribute(self.__name, self.__terminal, self.__prefix)

    def set_value(self, value: str) -> None:
        """Sets the value of the attribute."""
        self.__value = value

    @classmethod
    def from_json(cls, json: dict, terminals) -> "ComponentAttribute":
        """
        Constructs a ComponentAttribute object from JSON data.

        Args:
        - json (dict): The JSON data representing the attribute.

        Returns:
        - ComponentAttribute: A ComponentAttribute object constructed from the JSON data.
        """

        terminal_type = json["type"]
        terminal = terminals[terminal_type]
        if "prefix" in json:
            prefix = json["prefix"]
        else:
            prefix = ""
        return cls(json["name"], terminal, prefix)
