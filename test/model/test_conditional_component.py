import sys

import pytest

from src.model.form_spec import FormSpec

sys.path.append("../..")

from test.model.fixtures import *

from src.model.component_specifications.conditional_component_spec import \
    ConditionalComponentSpec
from src.model.components.conditional_component import ConditionalComponent


class TestConditionalComponent:
    @pytest.fixture
    def terminals(
        self,
        text_terminal,
        date_terminal,
        multi_choice_terminal,
        logical_operator_terminal,
    ):
        return [
            text_terminal,
            date_terminal,
            multi_choice_terminal,
            logical_operator_terminal,
        ]

    @pytest.fixture
    def attributes(
        self,
        text_attribute,
        date_attribute,
        multi_choice_attribute,
        logical_operator_attribute,
    ):
        return [
            text_attribute,
            date_attribute,
            multi_choice_attribute,
            logical_operator_attribute,
        ]

    @pytest.fixture
    def attribute_names(self, attributes):
        return [attribute.get_name() for attribute in attributes]

    @pytest.fixture
    def simple_type_specs(self, simple_type_spec_1, chain_type_spec_1):
        return [simple_type_spec_1, chain_type_spec_1]

    @pytest.fixture
    def chain_component_spec(self, simple_type_specs, attributes):
        return ChainComponentSpec(
            "chain_component",
            simple_type_specs,
            attributes,
            "components",
            "logical_operator",
            "chain_component",
        )

    @pytest.fixture
    def conditional_component_spec(self, chain_component_spec):
        conditional_type_specs = [
            FormSpec("if", "If Conditional"),
            FormSpec("if then", "If-Then Conditional"),
        ]
        return ConditionalComponentSpec(
            "conditional",
            conditional_type_specs,
            "components",
            "conditional",
            chain_component_spec.create_blank(),
            chain_component_spec.create_blank(),
        )

    def test_conditional_component(self, conditional_component_spec):
        conditional = ConditionalComponent(conditional_component_spec)
        conditional.reset_id(0, 0)
        assert (
            conditional.to_cola()
            == "[0] TEXT ADATE choice 1\nIF\n[1] TEXT ADATE choice 1"
        )

    def test_change_conditional_type(self, conditional_component_spec):
        conditional = ConditionalComponent(conditional_component_spec)
        conditional.set_form("if then")
        conditional.reset_id(0, 0)
        assert (
            conditional.to_cola()
            == "IF\n[0] TEXT ADATE choice 1\nTHEN\n[1] TEXT ADATE choice 1"
        )
