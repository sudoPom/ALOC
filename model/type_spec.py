from abc import ABC


class TypeSpec(ABC):
    def __init__(self, name, display_text, colour="Grey"):
        self.__name = name
        self.__display_text = display_text
        self.__colour = colour

    def get_name(self):
        return self.__name

    def get_display_text(self):
        return self.__display_text

    def get_colour(self):
        return self.__colour

    @classmethod
    def from_json(cls, json) -> "TypeSpec":
        return cls(
            json["type_name"], json["display_name"], cls.get_colour_from_json(json)
        )

    @staticmethod
    def get_colour_from_json(json):
        if "colour" in json:
            return json["colour"]
        return "grey"
