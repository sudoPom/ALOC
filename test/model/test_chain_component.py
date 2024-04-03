import sys

import pytest

from src.model.chain_parent import ChainParent

sys.path.append("../..")

from test.model.fixtures import *

from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.components.chain_component import ChainComponent


class TestChainComponent:
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

    @pytest.fixture()
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
            "chain_component",
            "logical_operator",
        )

    @pytest.fixture
    def chain_component(self, chain_component_spec) -> ChainComponent:
        parent = ChainParent(False)
        return ChainComponent(chain_component_spec, parent)

    def test_get_type(self, chain_component: ChainComponent):
        assert chain_component.get_form().get_name() == "type_1"

    def test_display_text(self, chain_component: ChainComponent):
        assert chain_component.to_cola() == "[0] TEXT ADATE choice 1"

    def test_change_type(self, chain_component: ChainComponent):
        chain_component.set_form("type_2")
        assert chain_component.to_cola() == "[0] choice 1 ADATE TEXT"

    def test_update_component(self, chain_component: ChainComponent):
        assert chain_component.to_cola() == "[0] TEXT ADATE choice 1"
        chain_component.update(
            subject="DIFFERENT TEXT",
            date=(HybridTerminal.CUSTOM_OPTION, "27 January 2002"),
            multi_choice="choice 2",
        )
        assert (
            chain_component.to_cola()
            == "[0] DIFFERENT TEXT on the 27 January 2002 choice 2"
        )

    def test_extend_component(self, chain_component: ChainComponent):
        assert chain_component.get_next() is None
        chain_component.add_next()
        next_component = chain_component.get_next()
        assert next_component is not None
        chain_component.update(
            subject="DIFFERENT TEXT",
            date=(HybridTerminal.CUSTOM_OPTION, "27 January 2002"),
            multi_choice="choice 2",
        )
        chain_component.reset_id(0, 0)
        assert (
            chain_component.to_cola()
            == "[0] DIFFERENT TEXT on the 27 January 2002 choice 2 and\n[1] TEXT ADATE choice 1"
        )
