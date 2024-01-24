class ComponentSpec:
    def __init__(self, name, types, location, component_type):
        self.__name = name
        self.__types = types
        self.__location = location
        self.__component_type = component_type

    def get_name(self):
        return self.__name

    def get_types(self):
        return self.__types

    def get_contract_location(self):
        return self.__location

    def get_component_type(self):
        return self.__component_type

    def get_location(self):
        return self.__location
