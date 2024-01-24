import tkinter as tk
from tkinter import filedialog

from model.components.contract import Contract
from view.renderer import Renderer
from view.scroll_canvas import ScrollCanvas


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller
        self.geometry("1000x1000")

        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")

        new_button = tk.Button(
            toolbar, text="Create New Contract", command=self.new_contract
        )
        new_button.pack(side="left")
        save_button = tk.Button(
            toolbar, text="Save Contract", command=self.save_contract
        )
        save_button.pack(side="left")
        load_button = tk.Button(
            toolbar, text="Open Contract", command=self.load_contract
        )
        load_button.pack(side="left")

        self.__tree_frame = ScrollCanvas(self)
        self.__tree_frame.pack(fill=tk.BOTH, expand=True)
        self.__renderer = Renderer(self.__tree_frame, controller, self.update_display)

        self.update_display()

    def update_display(self):
        """Re-draws the display with the contract that is currently stored."""
        contract = self.__controller.get_contract()
        self.render_contract(contract)

    def render_contract(self, contract: Contract, x=10, y=10):
        """Renders the contract

        Args:
            The contract to be rendered.
        """
        self.__renderer.render(x, y, contract)

    def save_contract(self):
        file_path = self.__controller.get_contract_path()
        if file_path is None:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".cola",
                filetypes=[("Cola files", "*.cola")],
            )
        if file_path:
            self.__controller.save_contract(file_path)
            print(f"Contract saved to: {file_path}")

    def load_contract(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".cola",
            filetypes=[("Cola files", "*.cola")],
        )
        if file_path:
            self.__controller.load_contract(file_path)
            self.update_display()
            print(f"Contract loaded from: {file_path}")

    def new_contract(self):
        self.__controller.create_new_contract()
        self.update_display()
