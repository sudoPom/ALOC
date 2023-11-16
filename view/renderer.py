from view.frames import *
import tkinter as tk

class Renderer:
    def __init__(self, frame, controller, re_render_func):
        self.__frame = frame
        self.__controller = controller
        self.__re_render_func = re_render_func

    def render_contract(self, x, y, contract):
        contract_button = ContractButton(self.__frame, self.__controller, self.__re_render_func)
        self.__frame.create_window(x, y, anchor=tk.NW, window=contract_button)
        for definition in contract.get_definitions():
            y += 50
            self.render_definition(definition, x + 20, y)

    def render_definition(self, definition, x, y):
        definition_button = SimpleDefinitionButton(self.__frame, definition, self.__re_render_func)
        self.__frame.create_window(x, y, anchor=tk.NW, window=definition_button)
            

