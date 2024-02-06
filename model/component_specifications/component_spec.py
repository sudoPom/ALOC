from typing import List

from model.type_spec import TypeSpec


class ComponentSpec:
    """
    ComponentSpec class represents the specifications of a component.

    Methods:
    - __init__(name, types, location, component_type): Initializes a ComponentSpec object.
    - get_name(): Retrieves the name of the component specification.
    - get_types(): Retrieves the list of type specifications associated with the component.
    - get_contract_location(): Retrieves the location of the component in the contract.
    - get_component_type(): Retrieves the type of the component.
    - get_location(): Retrieves the location of the component.
    - types_from_json(json): Converts JSON data into a list of TypeSpec objects.

    Attributes:
    - __name (str): The name of the component specification.
    - __types (List[TypeSpec]): The list of type specifications associated with the component.
    - __location (str): The location of the component in the contract.
    - __component_type (Type[Component]): The type of the component.
    """

    def __init__(
        self,
        name: str,
        types: List[TypeSpec],
        location: str,
        component_type: str,
    ) -> None:
        """
        Initializes a ComponentSpec object.

        Args:
        - name (str): The name of the component specification.
        - types (List[TypeSpec]): The list of type specifications associated with the component.
        - location (str): The location of the component in the contract.
        - component_type (Type[Component]): The type of the component.
        """
        self.__name = name
        self.__types = types
        self.__location = location
        self.__component_type = component_type

    def get_name(self) -> str:
        """Retrieves the name of the component specification."""
        return self.__name

    def get_types(self) -> List[TypeSpec]:
        """Retrieves the list of type specifications associated with the component."""
        return self.__types

    def get_contract_location(self) -> str:
        """Retrieves the location of the component in the contract."""
        return self.__location

    def get_component_type(self) -> str:
        """Retrieves the type of the component."""
        return self.__component_type

    def get_location(self) -> str:
        """Retrieves the location of the component."""
        return self.__location

    @staticmethod
    def types_from_json(json) -> List[TypeSpec]:
        """
        Converts JSON data into a list of TypeSpec objects.

        Args:
        - json: JSON data representing the type specifications.

        Returns:
        - List[TypeSpec]: A list of TypeSpec objects parsed from the JSON data.
        """
        return [TypeSpec.from_json(type_spec) for type_spec in json]
