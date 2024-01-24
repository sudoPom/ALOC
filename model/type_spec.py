class TypeSpec:
    def __init__(self, name, format_string, attributes, display_text, colour="Grey"):
        self.__name = name
        self.__format_string = format_string
        self.__expected_attributes = attributes
        self.__display_text = display_text
        self.__colour = colour

    def get_name(self):
        return self.__name

    def get_format_string(self):
        return self.__format_string

    def get_expected_attributes(self):
        return self.__expected_attributes

    def get_display_text(self):
        return self.__display_text

    def get_colour(self):
        return self.__colour
