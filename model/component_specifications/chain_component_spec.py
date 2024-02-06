from model.component_specifications.simple_component_spec import \
    SimpleComponentSpec


class ChainComponentSpec(SimpleComponentSpec):
    def __init__(self, name, types, attributes, location, component_type):
        super().__init__(name, types, attributes, location, component_type)

    @classmethod
    def from_json(cls, json, _):
        attributes = cls.attributes_from_json(json)
        type_specs = cls.type_specs_from_json(json)
        return cls(
            json["component_name"],
            type_specs,
            attributes,
            json["collection_location"],
            "chain_component",
        )
