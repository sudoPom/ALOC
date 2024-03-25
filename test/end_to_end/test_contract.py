import sys
from typing import Dict, List

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

    def update_component(
        self, contract, id: int, controller: Controller, update_dict: Dict
    ):
        component = self.get_component_by_id(contract, id)
        controller.update_component(component, update_dict)

    def test_simple(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/definition_only_spec.json"
        )
        controller.add_new_component("definition")
        assert contract.to_cola() == "[0] SUBJECT IS SUBJECT"

    def test_create_delete(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/definition_only_spec.json"
        )
        controller.add_new_component("definition")
        controller.delete_component(0)
        print(contract.to_cola())
        assert contract.to_cola() == ""

    def test_simple_update(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/definition_only_spec.json"
        )
        controller.add_new_component("definition")
        self.update_component(
            contract, 0, controller, {"Name": "BABA", "Definition": "YOU"}
        )
        assert contract.to_cola() == "[0] BABA IS YOU"

    def test_multi_update_and_delete(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/definition_only_spec.json"
        )
        for _ in range(4):
            controller.add_new_component("definition")
        self.update_component(
            contract, 0, controller, {"Name": "ROSE", "Definition": "RED"}
        )
        self.update_component(
            contract, 1, controller, {"Name": "VIOLET", "Definition": "BLUE"}
        )
        self.update_component(
            contract, 2, controller, {"Name": "FLAG", "Definition": "WIN"}
        )
        self.update_component(
            contract, 3, controller, {"Name": "BABA", "Definition": "YOU"}
        )

        assert (
            contract.to_cola()
            == "[0] ROSE IS RED\nC-AND\n[1] VIOLET IS BLUE\nC-AND\n[2] FLAG IS WIN\nC-AND\n[3] BABA IS YOU"
        )

        for _ in range(4):
            controller.delete_component(0)

        assert contract.to_cola() == ""

    def test_chain_component_extend_delete(self):
        controller, contract = self.create_controller(
            "./test/end_to_end/definition_only_spec.json"
        )
        controller.add_new_component("definition")
        component = self.get_component_by_id(contract, 0)
        controller.extend_chain_component(component)
        self.update_component(contract, 1, controller, {"Definition": "ALSO SUBJECT"})
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