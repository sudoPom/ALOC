class ComponentCollection:
    def __init__(self, name):
        self.__name = name
        self.__components = []
        self.__component_ids = set()

    def add_component(self, component):
        self.__components.append(component)
        self.__component_ids.add(component.get_id())

    def delete_component(self, component_id):
        self.__components = [
            component
            for component in self.__components
            if component.get_id() is not component_id
        ]
        self.__component_ids.remove(component_id)

    def get_name(self):
        return self.__name

    def contains_component(self, component_id):
        return component_id in self.__component_ids

    def get_component(self, component_id):
        for component in self.__components:
            if component.get_id() == component_id:
                return component
        raise ValueError("Component not found")

    def get_components(self):
        return self.__components
