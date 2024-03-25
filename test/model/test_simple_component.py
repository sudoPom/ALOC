import sys

import pytest

sys.path.append("../..")

from src.model.component_attribute import ComponentAttribute
from src.model.component_specifications.simple_component_spec import SimpleComponentSpec
from src.model.components.simple_component import SimpleComponent
from src.model.simple_type_spec import SimpleTypeSpec
from src.model.terminal_types.date_terminal import DateTerminal
from src.model.terminal_types.multi_choice_terminal import MultiChoiceTerminal
from src.model.terminal_types.text_terminal import TextTerminal


class TestComponents:
    @pytest.fixture
    def terminals(self):
        text_terminal = TextTerminal("subject", "TEXT", "subject", "")
        date_terminal = DateTerminal(
            "date", "ADATE", "27 January 2002", "date", "", ["ADATE", "custom date"]
        )
        multi_choice_terminal = MultiChoiceTerminal(
            "choice", "choice 1", ["choice 1", "choice 2"]
        )
        return [text_terminal, date_terminal, multi_choice_terminal]

    @pytest.fixture
    def attributes(self, terminals):
        attribute_1 = ComponentAttribute("subject", terminals[0])
        attribute_2 = ComponentAttribute("date", terminals[1])
        attribute_3 = ComponentAttribute("multichoice", terminals[2])
        return [attribute_1, attribute_2, attribute_3]

    @pytest.fixture
    def simple_type_specs(self, attributes):
        attribute_names_type_1 = [attribute.get_name() for attribute in attributes]
        attribute_names_type_2 = [
            attribute.get_name() for attribute in attributes[::-1]
        ]
        type_spec_1 = SimpleTypeSpec(
            "type_1", "{} {} {} {}", attribute_names_type_1, "type 1"
        )
        type_spec_2 = SimpleTypeSpec(
            "type_2", "{} {} {} {}", attribute_names_type_2, "type 2"
        )
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
    def simple_component(self, simple_component_spec) -> SimpleComponent:
        return SimpleComponent(simple_component_spec)

    def test_get_type(self, simple_component: SimpleComponent):
        assert simple_component.get_type().get_name() == "type_1"

    def test_display_text(self, simple_component: SimpleComponent):
        assert simple_component.get_display_text() == "0 TEXT ADATE choice 1"

    def test_change_type(self, simple_component: SimpleComponent):
        simple_component.set_type("type_2")
        assert simple_component.get_display_text() == "0 choice 1 ADATE TEXT"

    def test_update_component(self, simple_component: SimpleComponent):
        assert simple_component.get_display_text() == "0 TEXT ADATE choice 1"
        simple_component.update(
            subject="DIFFERENT TEXT",
            date=("custom date", "27 January 2002"),
            multichoice="choice 2",
        )
        assert (
            simple_component.get_display_text()
            == "0 DIFFERENT TEXT on the 27 January 2002 choice 2"
        )
