from typing import Tuple

from src.model.terminal_types.terminal import Terminal


class ComponentAttribute:
    """
    ComponentAttribute class Represents the attribute of a component.

    Args:
        name (str): The name of the attribute.
        terminal (:obj:`Terminal`): The terminal of this attribute.
        prefix (str, optional): The prefix to the attribute.
    """

    def __init__(self, name: str, terminal: Terminal, prefix: str = "") -> None:
        self.__name: str = name
        self.__terminal: Terminal = terminal
        self.__value: str | Tuple = terminal.get_default()
        self.__prefix = prefix

    def get_name(self) -> str:
        """
        Retrieves the name of the attribute.

        Returns:
            str: The name of this attribute.
        """
        return self.__name

    def get_terminal(self) -> Terminal:
        """
        Retrieves the terminal of the attribute.

        Returns:
            The terminal of this attribute.
        """
        return self.__terminal

    def get_value(self) -> str | Tuple:
        """
        Retrieves the value of the attribute.

        Returns:
            :obj:`str | Tuple`: The value of this attribute (with its prefix).

        Note:
            If the terminal was of type :obj:`HYBRID` the return type will be a tuple.
        """
        if type(self.__value) == str:
            return f"{self.__prefix}{self.__value}"
        print(self.__value[0])
        return (self.__value[0], f"{self.__prefix}{self.__value[1]}")

    def create_blank(self) -> "ComponentAttribute":
        """
        Creates a blank copy of this attribute.

        Returns:
            :obj:`ComponentAttribute`: A blank copy of this attribute.
        """
        return ComponentAttribute(self.__name, self.__terminal, self.__prefix)

    def set_value(self, value: str) -> None:
        """
        Sets the value of the attribute.

        Args:
            value (str): The value to set this attribute to.
        """
        self.__value = value

    @classmethod
    def from_json(cls, json: dict, terminals) -> "ComponentAttribute":
        """
        Constructs a ComponentAttribute object from JSON data.

        Args:
            json (:obj:`Dict`): The JSON data representing the attribute.

        Returns:
            :obj:`ComponentAttribute`: A ComponentAttribute object constructed from the JSON data.
        """

        terminal_type = json["type"]
        terminal = terminals[terminal_type]
        if "prefix" in json:
            prefix = json["prefix"]
        else:
            prefix = ""
        return cls(json["name"], terminal, prefix)
