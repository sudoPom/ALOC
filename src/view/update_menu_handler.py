import tkinter as tk
from collections import defaultdict
from typing import Callable

from src.controller.controller import Controller
from src.model.components.simple_component import SimpleComponent
from src.model.terminal_types.terminal import TerminalTypeNames


class UpdateFormEntry:
    """
    UpdateFormEntry class represents an entry in the update form.

    Methods:
    - __init__(entry_name, entry_type): Initializes an UpdateFormEntry object.
    - set_value(entry_value): Sets the value of the entry.
    - get_var(): Returns the variable of the entry.
    - get_value(): Returns the value of the entry.
    - get_type(): Returns the type of the entry.
    - get_name(): Returns the name of the entry.
    """

    def __init__(self, entry_name: str, terminal):
        """
        Initializes an UpdateFormEntry object.

        Args:
        - entry_name (str): The name of the entry.
        - entry_type: The type of the entry.
        """
        self.__name = entry_name
        self.__terminal = terminal
        self.__var = tk.StringVar()

    def set_value(self, entry_value: str) -> None:
        """
        Sets the value of the entry.

        Args:
        - entry_value (str): The value to set.
        """
        self.__var.set(entry_value)

    def get_var(self) -> tk.StringVar:
        """Returns the variable of the entry."""
        return self.__var

    def get_value(self) -> str:
        """Returns the value of the entry."""
        return self.__var.get()

    def get_terminal(self):
        """Returns the type of the entry."""
        return self.__terminal

    def get_name(self) -> str:
        """Returns the name of the entry."""
        return self.__name


class UpdateFormHandler:
    """
    UpdateFormHandler class manages the creation and handling of update forms for components.

    Methods:
    - create_update_form(root, component, re_render_func, controller): Creates an update form.
    - _create_submit_button(parent, entries, component, re_render_func, controller): Creates the submit button.
    - _create_entry_widgets(update_form, current_attributes): Creates entry widgets for attributes.
    - create_error_text(parent, row): Creates an error label widget.
    - _create_entry_method(parent, entry, row, entries): Creates entry widgets based on attribute types.
    - _create_entry_label(parent, text, row): Creates entry label widgets.
    - _create_entry_widget(parent, entry, row): Creates a basic text entry widget.
    - _create_option_widget(parent, entry, row): Creates a dropdown menu widget.
    - _create_date_widgets(parent, entry, row, custom_var): Creates date selection widgets.
    - update_button_state(button, entries, error_variable): Updates the state of the submit button.
    - _update(entries, update_form, component, controller, re_render_func): Updates the component.
    - _handle_date(entry_name, entry_var, date_dict): Handles date entry values.
    """

    def create_update_form(
        self,
        root: tk.Tk,
        component: SimpleComponent,
        re_render_func: Callable,
        controller: Controller,
    ) -> None:
        """
        Creates an update form.

        Args:
        - root (tk.Tk): The root Tkinter window.
        - component (Component): The component to update.
        - re_render_func (Callable): The function to call for re-rendering.
        - controller (Controller): The controller for managing component actions.
        """
        update_form = tk.Toplevel(root)
        update_form.geometry("1000x600")
        current_attributes = component.get_current_attributes()

        entries = self._create_entry_widgets(update_form, current_attributes)

        submit_button = self._create_submit_button(
            update_form, entries, component, re_render_func, controller
        )
        current_row = len(current_attributes)
        error_var = self.create_error_text(update_form, current_row)
        current_row += 1
        submit_button.grid(row=current_row, column=0, columnspan=2)

        for entry in entries:
            entry.get_var().trace_add(
                "write",
                lambda *_: self.update_button_state(submit_button, entries, error_var),
            )

    def _create_submit_button(
        self,
        parent: tk.Toplevel,
        entries: list,
        component: SimpleComponent,
        re_render_func: Callable,
        controller: Controller,
    ) -> tk.Button:
        """
        Creates the submit button.

        Args:
        - parent (tk.Toplevel): The parent window for the button.
        - entries (list): The list of entry widgets.
        - component (Component): The component to update.
        - re_render_func (Callable): The function to call for re-rendering.
        - controller (Controller): The controller for managing component actions.

        Returns:
        - tk.Button: The submit button.
        """
        submit_button = tk.Button(
            parent,
            text="Submit",
            command=lambda: self._update(
                entries, parent, component, controller, re_render_func
            ),
        )
        return submit_button

    def _create_entry_widgets(
        self, update_form: tk.Toplevel, current_attributes: list
    ) -> list:
        """
        Creates entry widgets for attributes.

        Args:
        - update_form (tk.Toplevel): The update form window.
        - current_attributes (list): The list of current attributes.

        Returns:
        - list: The list of entry widgets.
        """
        entries = []

        for i, attribute in enumerate(current_attributes):
            entry = UpdateFormEntry(attribute.get_name(), attribute.get_terminal())
            entries.append(entry)
            attribute_type = attribute.get_terminal().get_type()
            match attribute_type:
                case TerminalTypeNames.TEXT | TerminalTypeNames.MULTI_CHOICE:
                    entry.set_value(attribute.get_value())
                case TerminalTypeNames.DATE:
                    entry.set_value(attribute.get_value()[0])
                    custom_date_entry = UpdateFormEntry(
                        f"{attribute.get_name()}_custom", attribute.get_terminal()
                    )
                    custom_date_entry.set_value(attribute.get_value()[1])
                    entries.append(custom_date_entry)
                case _:
                    raise ValueError(f"Unsupported terminal type {attribute_type}")
            """
            if attribute.get_type() == Terminal.DATE:
                entry.set_value(attribute.get_value()[0])
                custom_date_entry = UpdateFormEntry(
                    f"{attribute.get_name()}_custom", attribute.get_type()
                )
                custom_date_entry.set_value(attribute.get_value()[1])
                entries.append(custom_date_entry)
            else:
                entry.set_value(attribute.get_value())
            """
            self._create_entry_label(
                update_form, attribute.get_name().replace("_", " "), i
            )
            self._create_entry_method(update_form, entry, i, entries)

        return entries

    def create_error_text(self, parent: tk.Toplevel, row: int) -> tk.StringVar:
        """
        Creates an error label widget.

        Args:
        - parent (tk.Toplevel): The parent window for the error label.
        - row (int): The row number for placing the label.

        Returns:
        - tk.StringVar: The error label widget.
        """
        error_val = tk.StringVar()
        error_label = tk.Label(
            parent,
            textvariable=error_val,
            fg="red",
            wraplength=600,
            justify=tk.LEFT,
        )
        error_label.grid(row=row, columnspan=2)
        return error_val

    def _create_entry_method(
        self,
        parent: tk.Toplevel,
        entry: UpdateFormEntry,
        row: int,
        entries: list,
    ) -> tk.Entry | tk.OptionMenu:
        """
        Creates entry widgets based on attribute types.

        Args:
        - parent (tk.Toplevel): The parent window for the entry widget.
        - entry (UpdateFormEntry): The entry to create.
        - row (int): The row number for placing the entry.
        - entries (list): The list of entry widgets.
        """
        terminal = entry.get_terminal()
        terminal_type = terminal.get_type()
        match terminal_type:
            case TerminalTypeNames.DATE:
                return self._create_date_widgets(
                    parent, entry, row, entries[-1].get_var()
                )
            case TerminalTypeNames.TEXT:
                return self._create_entry_widget(parent, entry, row)
            case TerminalTypeNames.MULTI_CHOICE:
                return self._create_option_widget(parent, entry, row)
            case _:
                raise ValueError(f"Invalid terminal type {terminal_type}")

    def _create_entry_label(self, parent: tk.Toplevel, text: str, row: int) -> None:
        """
        Creates entry label widgets.

        Args:
        - parent (tk.Toplevel): The parent window for the label.
        - text (str): The text of the label.
        - row (int): The row number for placing the label.
        """
        entry_label = tk.Label(parent, text=f"{text}:", justify=tk.RIGHT)
        entry_label.grid(row=row, column=0)

    @staticmethod
    def _create_entry_widget(
        parent: tk.Toplevel, entry: UpdateFormEntry, row: int
    ) -> tk.Entry:
        """
        Creates a basic text entry widget.

        Args:
        - parent (tk.Toplevel): The parent window for the entry widget.
        - entry (UpdateFormEntry): The entry to create.
        - row (int): The row number for placing the entry.

        Returns:
        - tk.Entry: The entry widget.
        """
        entry_widget = tk.Entry(parent, textvariable=entry.get_var())
        entry_widget.grid(row=row, column=1)
        return entry_widget

    @staticmethod
    def _create_option_widget(
        parent: tk.Toplevel, entry: UpdateFormEntry, row: int
    ) -> tk.OptionMenu:
        """
        Creates a dropdown menu widget.

        Args:
        - parent (tk.Toplevel): The parent window for the widget.
        - entry (UpdateFormEntry): The entry to create.
        - row (int): The row number for placing the widget.

        Returns:
        - tk.OptionMenu: The dropdown menu widget.
        """
        options = entry.get_terminal().get_choices()
        option_widget = tk.OptionMenu(parent, entry.get_var(), *options)
        option_widget.grid(row=row, column=1)
        return option_widget

    @staticmethod
    def _create_date_widgets(
        parent: tk.Toplevel,
        entry: UpdateFormEntry,
        row: int,
        custom_var: tk.StringVar,
    ) -> tk.OptionMenu:
        """
        Creates date selection widgets.

        Args:
        - parent (tk.Toplevel): The parent window for the widget.
        - entry (UpdateFormEntry): The entry to create.
        - row (int): The row number for placing the widget.
        - custom_var (tk.StringVar): The variable for the custom date entry.

        Returns:
        - tk.OptionMenu: The date selection widget.
        """
        terminal = entry.get_terminal()
        options = terminal.get_choices()
        date_widget = tk.OptionMenu(parent, entry.get_var(), *options)
        date_widget.grid(row=row, column=1)

        custom_entry = tk.Entry(parent, textvariable=custom_var)
        custom_entry.grid(row=row, column=2)

        def handle_option_change(_):
            selected_option = entry.get_value()
            print(selected_option)
            if selected_option == "custom date":
                custom_entry.grid(row=row, column=2)
            else:
                custom_var.set(terminal.get_default()[1])
                custom_entry.grid_forget()

        date_widget.bind("<Configure>", handle_option_change)

        return date_widget

    @staticmethod
    def update_button_state(
        button: tk.Button, entries: list, error_variable: tk.StringVar
    ) -> None:
        """
        Updates the state of the submit button.

        Args:
        - button (tk.Button): The submit button.
        - entries (list): The list of entry widgets.
        - error_variable (tk.StringVar): The variable for error messages.
        """
        for entry in entries:
            terminal = entry.get_terminal()
            if terminal.get_type() == TerminalTypeNames.MULTI_CHOICE:
                continue
            if not terminal.validate(entry.get_value()):
                button["state"] = "disabled"
                error_variable.set(terminal.get_explanation())
                return
        error_variable.set("")
        button["state"] = "normal"

    @staticmethod
    def _update(
        entries: list,
        update_form: tk.Toplevel,
        component: SimpleComponent,
        controller: Controller,
        re_render_func: Callable,
    ) -> None:
        """
        Updates the component represented by this frame and destroys the update form.

        Args:
        - entries (list): The list of entry widgets.
        - update_form (tk.Toplevel): The update form used to enter the component's sub-components.
        - component (Component): The component to be updated.
        - controller (Controller): The controller for managing component actions.
        - re_render_func (Callable): The function to call for re-rendering.
        """
        update_dict = dict()
        date_dict = defaultdict(lambda: ("", ""))
        for entry in entries:
            terminal = entry.get_terminal()
            if terminal.get_type() == TerminalTypeNames.DATE:
                UpdateFormHandler._handle_date(
                    entry.get_name(), entry.get_var(), date_dict
                )
            else:
                update_dict[entry.get_name()] = entry.get_value()
        for date_name, date in date_dict.items():
            update_dict[date_name] = date
        controller.update_component(component, update_dict)
        re_render_func()
        update_form.destroy()

    @staticmethod
    def _handle_date(
        entry_name: str, entry_var: tk.StringVar, date_dict: defaultdict
    ) -> None:
        """
        Handles date entry values.

        Args:
        - entry_name (str): The name of the date entry.
        - entry_var (tk.StringVar): The variable for the date entry.
        - date_dict (defaultdict): The dictionary for storing date values.
        """
        if entry_name.endswith("_custom"):
            date_entry = entry_name[:-7]
            current_date_value = date_dict[date_entry]
            date_dict[date_entry] = (current_date_value[0], entry_var.get())
        else:
            current_date_value = date_dict[entry_name]
            date_dict[entry_name] = (entry_var.get(), current_date_value[1])
