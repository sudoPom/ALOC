import sys
from typing import List

from src.model.component_collection import ComponentCollection

sys.path.append("../..")

from test.model.fixtures import *

from src.controller.controller import Controller
from src.model.aloc_spec import ALOCSpec
from src.model.model import Model


class TestContract:
    @staticmethod
    def create_controller(aloc_spec_path: str):
        spec_reader = ALOCSpec(aloc_spec_path)
        model = Model(
            spec_reader.get_contract_collections(), spec_reader.get_component_types()
        )
        controller = Controller(model, spec_reader.get_component_specs())
        return controller, controller.get_contract()

    @staticmethod
    def get_component_by_id(contract, id: int):
        componenet_collections: List[
            ComponentCollection
        ] = contract.get_component_collections()
        for component_collection in componenet_collections:
            try:
                return component_collection.get_component(id)
            except:
                continue
        raise ValueError(f"Component component id {id} not found in contract.")

    def test_simple(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        controller.add_new_component("definition")
        assert contract.to_cola() == "[0] SUBJECT IS SUBJECT"

    def test_create_delete(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        controller.add_new_component("definition")
        controller.delete_component(0)
        print(contract.to_cola())
        assert contract.to_cola() == ""

    def test_simple_update(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        controller.add_new_component("definition")
        controller.update_component(0, {"Name": "BABA", "Definition": "YOU"})
        assert contract.to_cola() == "[0] BABA IS YOU"

    def test_multi_update_and_delete(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        for _ in range(4):
            controller.add_new_component("definition")
        controller.update_component(0, {"Name": "ROSE", "Definition": "RED"})
        controller.update_component(1, {"Name": "VIOLET", "Definition": "BLUE"})
        controller.update_component(2, {"Name": "FLAG", "Definition": "WIN"})
        controller.update_component(3, {"Name": "BABA", "Definition": "YOU"})
        assert (
            contract.to_cola()
            == "[0] ROSE IS RED\nC-AND\n[1] VIOLET IS BLUE\nC-AND\n[2] FLAG IS WIN\nC-AND\n[3] BABA IS YOU"
        )

        for _ in range(4):
            controller.delete_component(0)

        assert contract.to_cola() == ""

    def test_chain_component_extend_delete(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        controller.add_new_component("definition")
        component = self.get_component_by_id(contract, 0)
        controller.extend_chain_component(0)
        controller.update_component(1, {"Definition": "ALSO SUBJECT"})
        assert (
            contract.to_cola()
            == "[0] SUBJECT IS SUBJECT AND\n[1] SUBJECT IS ALSO SUBJECT"
        )
        assert isinstance(component, ChainComponent)
        component.delete()
        assert contract.to_cola() == "[0] SUBJECT IS ALSO SUBJECT"
        component = self.get_component_by_id(contract, 0)
        assert isinstance(component, ChainComponent)
        component.delete()
        assert contract.to_cola() == ""

    def test_simple_component(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        controller.add_new_component("boring definition")
        controller.update_component(0, {"Name": "BABA", "Definition": "YOU"})
        assert contract.to_cola() == "[0] BABA IS YOU"

    def test_conditional_component(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        controller.add_new_component("conditional_definition")
        assert (
            contract.to_cola()
            == "[0] SUBJECT IS SUBJECT\nIF\n[1] it is the case that SUBJECT paid GBP 0 on ADATE"
        )
        controller.update_component(2, {"date": ("custom date", "27 January 2002")})
        assert (
            contract.to_cola()
            == "[0] SUBJECT IS SUBJECT\nIF\n[1] it is the case that SUBJECT paid GBP 0 on the 27 January 2002"
        )

    def test_actual_contract(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/relative_time_aloc_spec.json"
        )
        controller.add_new_component("conditional_statement")
        controller.add_new_component("statement")
        controller.extend_chain_component(2)
        controller.extend_chain_component(4)
        controller.change_component_type(0, "if then")
        controller.update_component(
            1,
            {
                "subject": "Alice",
                "verb_status": "paid",
                "object": "POUNDS 100",
                "date": ("custom date", "1 April 2001"),
                "logical_operator": "OR",
            },
        )
        controller.update_component(
            2,
            {
                "subject": "Alice",
                "verb_status": "paid",
                "object": "DOLLARS 120",
                "date": ("custom date", "1 April 2001"),
            },
        )
        controller.update_component(
            3,
            {
                "subject": "Bob",
                "modal_verb": "must",
                "verb": "deliver",
                "object": 'OTHEROBJECT "bicycle"',
                "date": ("custom date", "5 April 2001"),
            },
        )
        controller.update_component(
            4,
            {
                "subject": "Bob",
                "modal_verb": "may",
                "verb": "deliver",
                "object": 'REPORT "receipt"',
                "date": ("ANYDATE", "27 January 2002"),
            },
        )
        controller.update_component(
            5,
            {
                "subject": "Bob",
                "modal_verb": "is forbiddent to",
                "verb": "charge",
                "object": 'AMOUNT "delivery fee"',
                "date": ("ANYDATE", "27 January 2002"),
            },
        )
        assert (
            contract.to_cola()
            == """IF\n[0] it is the case that Alice paid POUNDS 100 on the 1 April 2001 OR\n[1] it is the case that Alice paid DOLLARS 120 on the 1 April 2001\nTHEN\n[2] it is the case that Bob must deliver OTHEROBJECT "bicycle" on the 5 April 2001\nC-AND\n[3] it is the case that Bob may deliver REPORT "receipt" ANYDATE AND\n[4] it is the case that Bob is forbiddent to charge AMOUNT "delivery fee" ANYDATE"""
        )
