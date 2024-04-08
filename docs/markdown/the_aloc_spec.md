# The ALOC Specification

The ALOC specification is a JSON file that determines the specifics of the components that the user can add to the contract. The ALOC specification has an object for specifying component collection ordering, a list of component specfications for each component type, and an object defining all of the terminal types.  The overall format looks something like this:

```json
{
  "contract": {},
  "simple_components": [],
  "chain_components": [],
  "conditional_components": [],
  "else_conditional_components": [],
  "terminal_types": {} 
}
```

This page will tell you all you need to know about modifying this specification for your specific use case.

## Contract

The contract object in the ALOC specification defines the ordering of the component collections of the contract. If ordering of components does not matter, then you can have a single component collection and set all the `component_location` fields of component objects to that component location. A contract must consist of at least one component collection. For example you may have something like this:

```json
"contract": {
    "collections" [
        "definitions",
        "other_components"
    ]
}
```
## Components

Components that can be used in ALOC are each defined as a list of component specifications. The fields required in a component specification can be found by looking at the documentation of the  corresponding `ComponentSpec` class' `from_json` method. 

For example, a chain component specification would look like this:

```json
"chain_components": [
    {
      "component_name": "definition",
      "linking_attribute": "logical_operator",
      "form_specs": [
        {
          "form_name": "subject pair",
          "format_string": "{} IS {}",
          "attributes": [
            "Name",
            "Definition"
          ],
          "display_name": "Subject-Pair Definition",
          "colour": "skyblue"
        },
      ],
      "attributes": [
        {
          "name": "Name",
          "type": "subject"
        },
        {
          "name": "Definition",
          "type": "subject"
        },
        {
          "name": "logical_operator",
          "type": "logical_and"
        }
      ],
      "collection_location": "definitions"
    }
```

For Components that reference other components (such as the `ConditionalComponent`) you must define the referenced components first. All defined ALOC components must be present, however if they are not required they can just be empty lists.

## Terminal Types

The terminal type object currently consists of a list of each of the defined terminal types: `multi_choice`, `text` and `hybrid`. Similarly to component specifications, the fields required for a terminal can be seen in the documentation for the respective `Terminal` class.

## Attributes

When specifying attributes you need to specify the following:
* `name`: The name of the attribute.
* `type`: The name of the terminal type of the attribute.

and optionally:
* `prefix`: The prefix of the attribute. (Does not effect the mu part of non terminals.).



