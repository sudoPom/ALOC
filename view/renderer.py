from view.frames import *
import tkinter as tk

class Renderer:
    def __init__(self, frame):
        self.__frame = frame

    def render_contract(self, x, y, contract):
        contract_frame = ContractFrame(self.__frame, contract)
        self.__frame.create_window(x, y, anchor=tk.NW, window=contract_frame)
        for definition in contract.get_definitions():
            y += 50
            self.render_definition(definition, x + 20, y)

    def render_definition(self, definition, x, y):
        definition_frame = SimpleDefinitionFrame(self.__frame, definition)
        self.__frame.create_window(x, y, anchor=tk.NW, window=definition_frame)
            

