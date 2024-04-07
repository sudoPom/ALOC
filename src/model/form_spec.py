from abc import ABC


class FormSpec(ABC):
    """
    Parent class for all form specification classes.
    """

    def __init__(self, name: str, display_text: str, colour: str = "Grey") -> None:
        """
            Initializes a FormSpec object.

        Args:
            name (str): The name of the form specification.
            display_text (str): The display text for the form specification.
            colour (str): The color of the widget for this specific form.

        """
        self.__name = name
        self.__display_text = display_text
        self.__colour = colour

    def get_name(self) -> str:
        """
        Returns the name of the form specification.

        Returns:
            str: The name of the form specification.
        """
        return self.__name

    def get_display_text(self) -> str:
        """
        Returns the display text of the form specification.

        Returns:
            str: The display text of the form specification.
        """
        return self.__display_text

    def get_colour(self) -> str:
        """
        Returns the color associated with the form specification.

        Returns:
            str: The color associated with the form specification.
        """
        return self.__colour

    @classmethod
    def from_json(cls, json: dict) -> "FormSpec":
        """
        Creates a FormSpec object from JSON data.

        Args:
            json (:obj:`Dict`): JSON data representing the FormSpec.

        Returns:
            :obj:`FormSpec`: A FormSpec object created from the JSON data.
        """
        return cls(
            json["form_name"], json["display_name"], cls.get_colour_from_json(json)
        )

    @staticmethod
    def get_colour_from_json(json: dict) -> str:
        """
        Returns the color from JSON data.

        Args:
            json (:obj:`Dict`): JSON data representing the FormSpec.

        Returns:
            str: The color retrieved from the JSON data.
        """
        if "colour" in json:
            return json["colour"]
        return "grey"
