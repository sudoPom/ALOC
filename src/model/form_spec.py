from abc import ABC


class FormSpec(ABC):
    """
    FormSpec class represents an abstract form specification.

    Methods:
    - __init__(name, display_text, colour="Grey"): Initializes a FormSpec object.
    - get_name(): Retrieves the name of the form specification.
    - get_display_text(): Retrieves the display text of the form specification.
    - get_colour(): Retrieves the color associated with the form specification.
    - from_json(json) -> FormSpec: Creates a FormSpec object from JSON data.
    - get_colour_from_json(json) -> str: Retrieves the color from JSON data.

    """

    def __init__(self, name: str, display_text: str, colour: str = "Grey") -> None:
        """
        Initializes a FormSpec object.

        Args:
        - name (str): The name of the form specification.
        - display_text (str): The display text of the form specification.
        - colour (str): The color associated with the type (default is "Grey").
        """
        self.__name = name
        self.__display_text = display_text
        self.__colour = colour

    def get_name(self) -> str:
        """
        Retrieves the name of the form specification.

        Returns:
        - str: The name of the form specification.
        """
        return self.__name

    def get_display_text(self) -> str:
        """
        Retrieves the display text of the form specification.

        Returns:
        - str: The display text of the form specification.
        """
        return self.__display_text

    def get_colour(self) -> str:
        """
        Retrieves the color associated with the form specification.

        Returns:
        - str: The color associated with the form specification.
        """
        return self.__colour

    @classmethod
    def from_json(cls, json: dict) -> "FormSpec":
        """
        Creates a FormSpec object from JSON data.

        Args:
        - json (dict): JSON data representing the FormSpec.

        Returns:
        - FormSpec: A FormSpec object created from the JSON data.
        """
        return cls(
            json["form_name"], json["display_name"], cls.get_colour_from_json(json)
        )

    @staticmethod
    def get_colour_from_json(json: dict) -> str:
        """
        Retrieves the color from JSON data.

        Args:
        - json (dict): JSON data representing the FormSpec.

        Returns:
        - str: The color retrieved from the JSON data.
        """
        if "colour" in json:
            return json["colour"]
        return "grey"
