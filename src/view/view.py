import tkinter as tk
from tkinter import filedialog

from model.components.contract import Contract
from view.constants import Constants
from view.renderer import Renderer
from view.scroll_canvas import ScrollCanvas


class View(tk.Tk):
    """
    View class represents the GUI view of the MVC architecture.

    Methods:
    - __init__(controller): Initializes a View object.
    - update_display(): Re-draws the display with the current contract.
    - render_contract(contract, x=10, y=10): Renders the given contract on the display.
    - _save_contract(): Saves the current contract to a file.
    - _load_contract(): Loads a contract from a file.
    - _new_contract(): Creates a new contract.
    """

    def __init__(self, controller) -> None:
        """
        Initializes a View object.

        Args:
        - controller: The controller object to interact with the model.
        """
        super().__init__()
        self.__controller = controller
        self.geometry("1000x1000")

        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")

        new_button = tk.Button(
            toolbar, text="Create New Contract", command=self._new_contract
        )
        new_button.pack(side="left")
        save_button = tk.Button(
            toolbar, text="Save Contract", command=self._save_contract
        )
        save_button.pack(side="left")
        load_button = tk.Button(
            toolbar, text="Open Contract", command=self._load_contract
        )
        load_button.pack(side="left")
        export_button = tk.Button(
            toolbar, text="Export Contract", command=self._export_to_cola
        )
        export_button.pack(side="left")
        self.__tree_frame = ScrollCanvas(self)
        self.__tree_frame.pack(fill=tk.BOTH, expand=True)
        self.__renderer = Renderer(self.__tree_frame, controller, self.update_display)

        self.update_display()

    def update_display(self) -> None:
        """Re-draws the display with the contract that is currently stored."""
        contract = self.__controller.get_contract()
        self.render_contract(contract)

    def render_contract(self, contract: Contract, x=10, y=10):
        """
        Renders the given contract on the display.

        Args:
        - contract (Contract): The contract to be rendered.
        - x (int): The x-coordinate of the contract's rendering.
        - y (int): The y-coordinate of the contract's rendering.
        """
        self.__renderer.render(x, y, contract)

    def _save_contract(self) -> None:
        """Saves the current contract to a file."""
        file_path = self.__controller.get_contract_path()
        if file_path == "":
            file_path = filedialog.asksaveasfilename(
                defaultextension=f".{Constants.FILE_EXT}",
                filetypes=[
                    (f".{Constants.FILE_TYPE_NAME} files", f"*.{Constants.FILE_EXT}")
                ],
            )
        if file_path:
            self.__controller.save_contract(file_path)
            print(f"Contract saved to: {file_path}")

    def _load_contract(self) -> None:
        """Loads a contract from a file."""
        file_path = filedialog.askopenfilename(
            defaultextension=f".{Constants.FILE_EXT}",
            filetypes=[
                (f"{Constants.FILE_TYPE_NAME} files", f"*.{Constants.FILE_EXT}")
            ],
        )
        if file_path:
            self.__controller.load_contract(file_path)
            self.update_display()
            print(f"Contract loaded from: {file_path}")

    def _new_contract(self) -> None:
        """Creates a new contract."""
        self.__controller.create_new_contract()
        self.update_display()

    def _export_to_cola(self) -> None:
        file_path = filedialog.asksaveasfilename(
            defaultextension=f".{Constants.TEXT_EXT}",
            filetypes=[(f"{Constants.TEXT_EXT} files", f"*.{Constants.TEXT_EXT}")],
        )
        if file_path:
            self.__controller.export_to_cola(file_path)
            print(f"Contract exported to: {file_path}")
