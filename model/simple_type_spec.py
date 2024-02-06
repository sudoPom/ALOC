from model.type_spec import TypeSpec


class SimpleTypeSpec(TypeSpec):
    def __init__(self, name, format_string, attributes, display_text, colour="Grey"):
        super().__init__(name, display_text, colour)
        self.__format_string = format_string
        self.__expected_attributes = attributes

    def get_format_string(self):
        return self.__format_string

    def get_expected_attributes(self):
        return self.__expected_attributes

    @classmethod
    def from_json(cls, json):
        return cls(
            json["type_name"],
            json["format_string"],
            json["attributes"],
            json["display_name"],
            super().get_colour_from_json(json),
        )
