from typing import List

from src.model.form_spec import FormSpec


class SimpleFormSpec(FormSpec):
    """
    SimpleFormSpec class represents a simple form specification, containing attributes.

    Args:
        name (str): The name of the form specification.
        format_string (str): The format string used to display the component.
        attributes (:obj:`List[str]`): The list of expected attributes.
        display_text (str): The display text for the form specification.
        colour (str): The color of the widget for this specific form.
    """

    def __init__(
        self,
        name: str,
        format_string: str,
        attributes: List[str],
        display_text: str,
        colour: str = "Grey",
    ) -> None:
        super().__init__(name, display_text, colour)
        self.__format_string = format_string
        self.__expected_attributes = attributes

    def get_format_string(self) -> str:
        """
        Retrieves the format string for the type specification.

        Returns:
            str: The format string.
        """
        return self.__format_string

    def get_expected_attributes(self) -> List[str]:
        """
        Retrieves the list of names of attributes used in this form.

        Returns:
            :obj:`List[str]`: The list of expected attributes.
        """
        return self.__expected_attributes

    @classmethod
    def from_json(cls, json: dict) -> "SimpleFormSpec":
        """
        Creates a :obj:`SimpleTypeSpec` object from JSON data.

        Args:
            json (:obj:`dict`): JSON data representing the SimpleTypeSpec.

        Returns:
            :obj:`SimpleTypeSpec`: A SimpleTypeSpec object created from the JSON data.
        """
        return SimpleFormSpec(
            json["form_name"],
            json["format_string"],
            json["attributes"],
            json["display_name"],
            super().get_colour_from_json(json),
        )
