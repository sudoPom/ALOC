import tkinter as tk

from controller.controller import Controller
from model.contract import Contract


class View:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
    
    def update_display(self):
        """Re-draws the display with the contract that is currently stored."""
        contract = self.controller.get_contract()
        render_contract(contract)


    def render_contract(contract: Contract):
        """Renders the contract

        Args:
            The contract to be rendered.
        """
        pass
