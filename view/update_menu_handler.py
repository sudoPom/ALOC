import tkinter as tk
from collections import defaultdict

from view.non_terminal_types import ContractNonTerminal


class UpdateFormHandler:
    def create_update_form(self, root, component, re_render_func, controller):
        update_form = tk.Toplevel(root)
        update_form.geometry("1000x600")
        current_components = component.get_current_components()

        entries = self._create_entry_widgets(update_form, current_components)

        submit_button = self._create_submit_button(
            update_form, entries, component, re_render_func, controller
        )
        current_row = len(current_components)
        error_var = self.create_error_text(update_form, current_row)
        current_row += 1
        submit_button.grid(row=current_row, column=0, columnspan=2)

        for entry in entries:
            entry.get_var().trace_add(
                "write",
                lambda *_: self.update_button_state(submit_button, entries, error_var),
            )

    def _create_submit_button(
        self, parent, entries, component, re_render_func, controller
    ):
        submit_button = tk.Button(
            parent,
            text="Submit",
            command=lambda: self._update(
                entries, parent, component, controller, re_render_func
            ),
        )
        return submit_button

    def _create_entry_widgets(self, update_form, current_components):
        entries = []

        for i, (entry_name, [entry_value, entry_type]) in enumerate(
            current_components.items()
        ):
            entry = UpdateFormEntry(entry_name, entry_type)
            entries.append(entry)
            if entry_type == ContractNonTerminal.DATE:
                entry.set_value(entry_value[0])
                custom_date_entry = UpdateFormEntry(f"{entry_name}_custom", entry_type)
                custom_date_entry.set_value(entry_value[1])
                entries.append(custom_date_entry)
            else:
                entry.set_value(entry_value)
            self._create_entry_label(update_form, entry_name.replace("_", " "), i)
            self._create_entry_method(
                update_form,
                entry,
                i,
                entries,
            )

        return entries

    def create_error_text(self, parent, row):
        error_val = tk.StringVar()
        error_label = tk.Label(
            parent, textvariable=error_val, fg="red", wraplength=600, justify=tk.LEFT
        )
        error_label.grid(row=row, columnspan=2)
        return error_val

    def _create_entry_method(self, parent, entry, row, entries):
        entry_type = entry.get_type()
        if entry_type == ContractNonTerminal.DATE:
            return self._create_date_widgets(parent, entry, row, entries[-1].get_var())
        if ContractNonTerminal.is_optional(entry_type):
            return self._create_option_widget(parent, entry, row)
        return self._create_entry_widget(parent, entry, row)

    def _create_entry_label(self, parent, text, row):
        entry_label = tk.Label(parent, text=f"{text}:", justify=tk.RIGHT)
        entry_label.grid(row=row, column=0)

    @staticmethod
    def _create_entry_widget(parent, entry, row):
        """Creates a basic text entry widget."""
        entry_widget = tk.Entry(parent, textvariable=entry.get_var())
        entry_widget.grid(row=row, column=1)
        return entry_widget

    @staticmethod
    def _create_option_widget(parent, entry, row):
        """Creates a dropdown menu for the user to select from."""
        options = ContractNonTerminal.get_options(entry.get_type())
        option_widget = tk.OptionMenu(parent, entry.get_var(), *options)
        option_widget.grid(row=row, column=1)
        return option_widget

    @staticmethod
    def _create_date_widgets(parent, entry, row, custom_var):
        """
        Creates two widgets, one for selecting the type of date and the other
        for selecting a custom date.
        """
        options = ContractNonTerminal.get_options(ContractNonTerminal.DATE)
        date_widget = tk.OptionMenu(parent, entry.get_var(), *options)
        date_widget.grid(row=row, column=1)

        custom_entry = tk.Entry(parent, textvariable=custom_var)
        custom_entry.grid(row=row, column=2)

        def handle_option_change(_):
            selected_option = entry.get_value()
            if selected_option == "custom date":
                custom_entry.grid(row=row, column=2)
            else:
                custom_var.set("27 January 2002")
                custom_entry.grid_forget()

        date_widget.bind("<Configure>", handle_option_change)

        return date_widget

    @staticmethod
    def update_button_state(button, entries, error_variable):
        """Disables the submit button if any of the entries are invalid."""
        for entry in entries:
            if not ContractNonTerminal.validate_entry(
                entry.get_value(), entry.get_type()
            ):
                button["state"] = "disabled"
                error_variable.set(
                    ContractNonTerminal.error_explanation(entry.get_type())
                )
                return
        error_variable.set("")
        button["state"] = "normal"

    @staticmethod
    def _update(entries, update_form, component, controller, re_render_func):
        """
        Updates the component represented by this frame and destroys
        the update form.

        Args:
        - entries: The entries that the user has entered.
        - update_form: The update form used to enter the
        component's sub-components.
        - component: The component to be updated.
        """
        update_dict = dict()
        date_dict = defaultdict(lambda: ("", ""))
        for entry in entries:
            if entry.get_type() == ContractNonTerminal.DATE:
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
    def _handle_date(entry_name, entry_var, date_dict):
        if entry_name.endswith("_custom"):
            date_entry = entry_name[:-7]
            current_date_value = date_dict[date_entry]
            date_dict[date_entry] = (current_date_value[0], entry_var.get())
        else:
            current_date_value = date_dict[entry_name]
            date_dict[entry_name] = (entry_var.get(), current_date_value[1])


class UpdateFormEntry:
    def __init__(self, entry_name: str, entry_type):
        self.name = entry_name
        self.entry_type = entry_type
        self.var = tk.StringVar()

    def set_value(self, entry_value: str):
        self.var.set(entry_value)

    def get_var(self):
        return self.var

    def get_value(self):
        return self.var.get()

    def get_type(self):
        return self.entry_type

    def get_name(self):
        return self.name
