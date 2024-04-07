import sys

import pytest

sys.path.append("../..")

from test.model.fixtures import *

from src.model.component_specifications.simple_component_spec import \
    SimpleComponentSpec
from src.model.components.simple_component import SimpleComponent
from src.model.simple_form_spec import SimpleFormSpec


class TestSimpleComponent:
    @pytest.fixture
    def terminals(
        self,
        text_terminal,
        date_terminal,
        multi_choice_terminal,
    ):
        return [
            text_terminal,
            date_terminal,
            multi_choice_terminal,
        ]

    @pytest.fixture
    def attributes(
        self,
        text_attribute,
        date_attribute,
        multi_choice_attribute,
    ):
        return [
            text_attribute,
            date_attribute,
            multi_choice_attribute,
        ]

    @pytest.fixture
    def simple_type_specs(self, attributes):
        attribute_names_type_1 = [attribute.get_name() for attribute in attributes]
        attribute_names_type_2 = [
            attribute.get_name() for attribute in attributes[::-1]
        ]
        type_spec_1 = SimpleFormSpec(
            "type_1", "{} {} {}", attribute_names_type_1, "type 1"
        )
        type_spec_2 = SimpleFormSpec(
            "type_2", "{} {} {}", attribute_names_type_2, "type 2"
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
        assert simple_component.get_form().get_name() == "type_1"

    def test_display_text(self, simple_component: SimpleComponent):
        assert simple_component.to_cola() == "[0] TEXT ADATE choice 1"

    def test_change_type(self, simple_component: SimpleComponent):
        simple_component.set_form("type_2")
        assert simple_component.to_cola() == "[0] choice 1 ADATE TEXT"

    def test_update_component(self, simple_component: SimpleComponent):
        assert simple_component.to_cola() == "[0] TEXT ADATE choice 1"
        simple_component.update(
            subject="DIFFERENT TEXT",
            date=(HybridTerminal.CUSTOM_OPTION, "27 January 2002"),
            multi_choice="choice 2",
        )
        assert (
            simple_component.to_cola()
            == "[0] DIFFERENT TEXT on the 27 January 2002 choice 2"
        )
