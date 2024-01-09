import tkinter as tk
from collections import defaultdict

from view.non_terminal_types import ContractNonTerminal


class UpdateFormHandler:
    def create_update_form(self, root, component, re_render_func, controller):
        update_form = tk.Toplevel(root)
        current_components = component.get_current_components()

        entries = self._create_entry_widgets(update_form, current_components)

        submit_button = self._create_submit_button(
            update_form, entries, component, re_render_func, controller
        )
        submit_button.grid(row=len(current_components), column=0, columnspan=2)

        for _, _, var in entries:
            var.trace_add(
                "write",
                lambda *_: self.update_button_state(submit_button, entries),
            )

    def _create_submit_button(
        self, parent, entry_vars_and_types, component, re_render_func, controller
    ):
        submit_button = tk.Button(
            parent,
            text="Submit",
            command=lambda: self._update(
                entry_vars_and_types, parent, component, controller, re_render_func
            ),
        )
        return submit_button

    def _create_entry_widgets(self, update_form, current_components):
        entries = []

        for i, (entry_name, [entry_value, entry_type]) in enumerate(
            current_components.items()
        ):
            entry_var = tk.StringVar()
            entries.append((entry_name, entry_type, entry_var))
            if entry_type == ContractNonTerminal.DATE:
                custom_date_entry_var = tk.StringVar()
                entries.append(
                    (
                        f"{entry_name}_custom",
                        ContractNonTerminal.DATE,
                        custom_date_entry_var,
                    )
                )
            self._create_entry_label(update_form, entry_name, i)
            self._create_entry_method(
                update_form, entry_var, entry_value, entry_type, i, entries
            )

        return entries

    def _create_entry_method(
        self, parent, entry_var, entry_value, entry_type, row, entries
    ):
        if entry_type == ContractNonTerminal.DATE:
            return self._create_date_widgets(
                parent, entry_var, entry_value, row, entries[-1][2]
            )
        if ContractNonTerminal.is_optional(entry_type):
            return self._create_option_widget(
                parent, entry_var, entry_value, entry_type, row
            )
        return self._create_entry_widget(parent, entry_var, entry_value, row)

    def _create_entry_label(self, parent, text, row):
        entry_label = tk.Label(parent, text=f"{text}:")
        entry_label.grid(row=row, column=0)

    @staticmethod
    def _create_entry_widget(parent, entry_var, entry_value, row):
        """Creates a basic text entry widget."""
        entry_widget = tk.Entry(parent, textvariable=entry_var)
        entry_widget.insert(0, entry_value)
        entry_widget.grid(row=row, column=1)
        return entry_widget

    @staticmethod
    def _create_option_widget(parent, entry_var, entry_value, entry_type, row):
        """Creates a dropdown menu for the user to select from."""
        options = ContractNonTerminal.get_options(entry_type)
        entry_var.set(entry_value)
        option_widget = tk.OptionMenu(parent, entry_var, *options)
        option_widget.grid(row=row, column=1)
        return option_widget

    @staticmethod
    def _create_date_widgets(parent, entry_var, entry_value, row, custom_var):
        """
        Creates two widgets, one for selecting the type of date and the other
        for selecting a custom date.
        """
        options = ContractNonTerminal.get_options(ContractNonTerminal.DATE)
        entry_var.set(entry_value[0])
        date_widget = tk.OptionMenu(parent, entry_var, *options)
        date_widget.grid(row=row, column=1)

        custom_entry = tk.Entry(parent, textvariable=custom_var)
        custom_entry.grid(row=row, column=2)
        custom_entry.insert(0, entry_value[1])

        def handle_option_change(_):
            selected_option = entry_var.get()
            if selected_option == "custom date":
                custom_entry.grid(row=row, column=2)
            else:
                custom_entry.grid_forget()

        date_widget.bind("<Configure>", handle_option_change)

        return date_widget

    @staticmethod
    def update_button_state(button, entry_vars_and_types):
        """Disables the submit button if any of the entries are invalid."""
        button["state"] = (
            "normal"
            if all(
                ContractNonTerminal.validate_entry(var.get(), entry_type)
                for _, (_, entry_type, var) in enumerate(entry_vars_and_types)
            )
            else "disabled"
        )

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
        for entry_name, entry_type, entry_var in entries:
            if entry_type == ContractNonTerminal.DATE:
                UpdateFormHandler._handle_date(entry_name, entry_var, date_dict)
            else:
                update_dict[entry_name] = entry_var.get()
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
