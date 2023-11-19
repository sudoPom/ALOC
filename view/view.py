import tkinter as tk

from controller.controller import Controller
from model.contract import Contract
from view.zoom_pan_canvas import ZoomPanCanvas
from view.renderer import Renderer


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__tree_frame = ZoomPanCanvas(self)
        self.__tree_frame.pack(fill=tk.BOTH, expand=True)
        self.__renderer = Renderer(
            self.__tree_frame, controller, self.update_display)
        self.update_display()

    def update_display(self):
        """Re-draws the display with the contract that is currently stored."""
        contract = self.controller.get_contract()
        self.render_contract(contract)

    def render_contract(self, contract: Contract, x=10, y=10):
        """Renders the contract

        Args:
            The contract to be rendered.
        """
        self.__renderer.render_contract(x, y, contract)
