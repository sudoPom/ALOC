from view.frames import contract_frame, simple_definition_frame
import tkinter as tk

PADDING_PX = 10
INDENT_SIZE_PX = 20


class Renderer:
    def __init__(self, frame, controller, re_render_func):
        self.__frame = frame
        self.__controller = controller
        self.__re_render_func = re_render_func

    def render_contract(self, x, y, contract):
        self.__frame.delete("all")
        contract_frame_widget = contract_frame.ContractFrame(
            self.__frame, self.__controller, self.__re_render_func)
        self.__frame.create_window(
            x, y, anchor=tk.NW, window=contract_frame_widget)
        self.__frame.update()
        y += contract_frame_widget.winfo_reqheight()
        for definition in contract.get_definitions():
            y += PADDING_PX
            rendered_definition = self.render_definition(
                definition, x + INDENT_SIZE_PX, y)
            self.__frame.update()
            y += rendered_definition.winfo_reqheight()

    def render_definition(self, definition, x, y):
        definition_frame_widget = simple_definition_frame.SimpleDefinitionFrame(
            self.__frame, self.__controller, definition, self.__re_render_func)
        self.__frame.create_window(
            x, y, anchor=tk.NW, window=definition_frame_widget)
        return definition_frame_widget
