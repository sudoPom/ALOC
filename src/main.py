from controller.controller import Controller
from model.aloc_spec import ALOCSpec
from model.model import Model
from view.view import View


class App:
    def __init__(self) -> None:
        spec_reader = ALOCSpec("./relative_time_aloc_spec.json")
        self.model = Model(
            spec_reader.get_contract_collections(), spec_reader.get_component_types()
        )
        self.controller = Controller(self.model, spec_reader.get_component_specs())
        self.view = View(self.controller)

    def main_loop(self) -> None:
        self.view.mainloop()


if __name__ == "__main__":
    app = App()
    app.main_loop()
