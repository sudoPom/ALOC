import sys

import pytest

sys.path.append("../..")

from src.model.chain_parent import ChainParent
from src.model.component_attribute import ComponentAttribute
from src.model.component_specifications.chain_component_spec import \
    ChainComponentSpec
from src.model.components.chain_component import ChainComponent
from src.model.simple_form_spec import SimpleFormSpec
from src.model.terminal_types.hybrid_terminal import HybridTerminal
from src.model.terminal_types.multi_choice_terminal import MultiChoiceTerminal
from src.model.terminal_types.text_terminal import TextTerminal


@pytest.fixture
def terminals():
    multi_choice_terminal = MultiChoiceTerminal(
        "choice", "choice 1", ["choice 1", "choice 2"], False
    )
    return [text_terminal, date_terminal, multi_choice_terminal]


@pytest.fixture
def date_terminal():
    return HybridTerminal(
        "date", "ADATE", "27 January 2002", "date", "", ["ADATE", "custom date"]
    )


@pytest.fixture
def text_terminal():
    return TextTerminal("subject", "TEXT", "subject", "")


@pytest.fixture
def multi_choice_terminal():
    return MultiChoiceTerminal("choice", "choice 1", ["choice 1", "choice 2"], False)


@pytest.fixture
def logical_operator_terminal():
    return MultiChoiceTerminal("logical_operator", "and", ["and", "or"], False)


@pytest.fixture
def text_attribute(text_terminal):
    return ComponentAttribute("subject", text_terminal)


@pytest.fixture
def date_attribute(date_terminal):
    return ComponentAttribute("date", date_terminal, "on the ")


@pytest.fixture
def multi_choice_attribute(multi_choice_terminal):
    return ComponentAttribute("multi_choice", multi_choice_terminal)


@pytest.fixture
def logical_operator_attribute(logical_operator_terminal):
    return ComponentAttribute("logical_operator", logical_operator_terminal)


@pytest.fixture
def simple_type_spec_1(attributes):
    attribute_names_type_1 = [attribute.get_name() for attribute in attributes]
    return SimpleFormSpec("type_1", "{} {} {}", attribute_names_type_1, "type 1")


@pytest.fixture
def simple_type_spec_2(attributes):
    attribute_names_type_2 = [attribute.get_name() for attribute in attributes[::-1]]
    return SimpleFormSpec("type_2", "{} {} {}", attribute_names_type_2, "type 2")


@pytest.fixture
def chain_type_spec_1(attributes):
    attribute_names_type_2 = [attribute.get_name() for attribute in attributes[::-1]][
        1:
    ]
    return SimpleFormSpec("type_2", "{} {} {}", attribute_names_type_2, "type 2")


@pytest.fixture
def chain_component_spec(simple_type_specs, attributes):
    return ChainComponentSpec(
        "chain_component",
        simple_type_specs,
        attributes,
        "components",
        "and",
        "chain_component",
    )


@pytest.fixture
def chain_component(chain_component_spec) -> ChainComponent:
    parent = ChainParent(False)
    return ChainComponent(chain_component_spec, parent)
