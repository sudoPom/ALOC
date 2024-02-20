from typing import Tuple

from view.terminal_types import Terminal


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

    def __init__(self, name: str, attribute_type: Terminal) -> None:
        """
        Initializes a ComponentAttribute object.

        Args:
        - name (str): The name of the attribute.
        - attribute_type (Terminal): The type of the attribute.
        """
        self.__name: str = name
        self.__attribute_type: Terminal = attribute_type
        self.__value: str | Tuple = attribute_type.value

    def get_name(self) -> str:
        """Retrieves the name of the attribute."""
        return self.__name

    def get_type(self) -> Terminal:
        """Retrieves the type of the attribute."""
        return self.__attribute_type

    def get_value(self) -> str | Tuple:
        """Retrieves the value of the attribute."""
        return self.__value

    def create_blank(self):
        return ComponentAttribute(self.__name, self.__attribute_type)

    def set_value(self, value: str) -> None:
        """Sets the value of the attribute."""
        self.__value = value

    @classmethod
    def from_json(cls, json: dict) -> "ComponentAttribute":
        """
        Constructs a ComponentAttribute object from JSON data.

        Args:
        - json (dict): The JSON data representing the attribute.

        Returns:
        - ComponentAttribute: A ComponentAttribute object constructed from the JSON data.
        """
        attribute_type: Terminal = Terminal.from_string(json["type"])
        return cls(json["name"], attribute_type)
