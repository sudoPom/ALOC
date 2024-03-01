import sys
from unittest.mock import Mock

import pytest

sys.path.append("../../src")

from model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from model.components.simple_component import SimpleComponent
from model.simple_type_spec import SimpleTypeSpec
from model.terminal_types.date_terminal import DateTerminal
from model.terminal_types.multi_choice_terminal import MultiChoiceTerminal
from model.terminal_types.text_terminal import TextTerminal
from src.model.component_attribute import ComponentAttribute


class TestComponents:
    @pytest.fixture
    def terminals(self):
        text_terminal = Mock(TextTerminal)
        text_terminal.get_parse_root.side_effect = lambda: "subject"
        date_terminal = Mock(DateTerminal)
        multi_choice_terminal = Mock(MultiChoiceTerminal)
        return [text_terminal]

    @pytest.fixture
    def attributes(self, terminals):
        attribute_1 = ComponentAttribute("attribute_1", terminals[0])
        attribute_2 = ComponentAttribute("attribute_2", terminals[1])
        attribute_3 = ComponentAttribute("attribute_3", terminals[2])
        return [attribute_1, attribute_2, attribute_3]

    @pytest.fixture
    def simple_type_specs(self, attributes):
        type_spec_1 = SimpleTypeSpec("type_1", "{}", attributes, "type 1")
        type_spec_2 = SimpleTypeSpec("type_2", "{}", attributes, "type 2")
        return [type_spec_1, type_spec_2]

    @pytest.fixture
    def simple_component_spec(self, simple_type_specs, attributes):
        return SimpleComponentSpec(
            "simple_component",
            simple_type_specs,
            attributes,
            "components",
            "simple_component",
        )

    @pytest.fixture
    def simple_component(self, component_spec):
        return SimpleComponent(component_spec)

    def test_get_type(self, component):
        assert component.get_type().get_name() == "type_1"
