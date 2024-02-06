from typing import List

from model.type_spec import TypeSpec


class SimpleTypeSpec(TypeSpec):
    """
    SimpleTypeSpec class represents a simple type specification.

    This class inherits from TypeSpec.

    Methods:
    - __init__(name, format_string, attributes, display_text, colour="Grey"): Initializes a SimpleTypeSpec object.
    - get_format_string(): Retrieves the format string for the type specification.
    - get_expected_attributes(): Retrieves the list of expected attributes.
    - from_json(json) -> SimpleTypeSpec: Creates a SimpleTypeSpec object from JSON data.

    """

    def __init__(
        self,
        name: str,
        format_string: str,
        attributes: List[str],
        display_text: str,
        colour: str = "Grey",
    ) -> None:
        """
        Initializes a SimpleTypeSpec object.

        Args:
        - name (str): The name of the type specification.
        - format_string (str): The format string used to display the type.
        - attributes (List[str]): The list of expected attributes.
        - display_text (str): The display text for the type specification.
        - colour (str): The color associated with the type (default is "Grey").
        """
        super().__init__(name, display_text, colour)
        self.__format_string = format_string
        self.__expected_attributes = attributes

    def get_format_string(self) -> str:
        """
        Retrieves the format string for the type specification.

        Returns:
        - str: The format string.
        """
        return self.__format_string

    def get_expected_attributes(self) -> List[str]:
        """
        Retrieves the list of expected attributes.

        Returns:
        - List[str]: The list of expected attributes.
        """
        return self.__expected_attributes

    @classmethod
    def from_json(cls, json: dict) -> "SimpleTypeSpec":
        """
        Creates a SimpleTypeSpec object from JSON data.

        Args:
        - json (dict): JSON data representing the SimpleTypeSpec.

        Returns:
        - SimpleTypeSpec: A SimpleTypeSpec object created from the JSON data.
        """
        return SimpleTypeSpec(
            json["type_name"],
            json["format_string"],
            json["attributes"],
            json["display_name"],
            super().get_colour_from_json(json),
        )
