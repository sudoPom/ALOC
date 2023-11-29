import tkinter as tk
from view.non_terminal_types import ContractNonTerminal
from controller.controller import Controller
from collections import defaultdict


class BaseFrame(tk.Frame):
    def __init__(self, parent, controller, colour, button_text, re_render_func, component=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.__colour = colour
        self.__text = button_text
        self.__menu = None
        self.__component = component
        self.create_widgets()

    def get_text(self):
        return self.__text

    def get_colour(self):
        return self.__colour

    def get_controller(self):
        return self.__controller

    def get_menu(self):
        return self.__menu

    def trigger_re_render(self):
        self.__re_render_func()

    def create_widgets(self):
        raise NotImplementedError(
            "Base class method for create_widgets should be overridden")

    def show_menu(self, event):
        self.__menu.tk_popup(event.x_root, event.y_root)

    def change_component_type(self, component_type):
        Controller.change_component_type(self.__component, component_type)
        self.trigger_re_render()

    def add_type_submenu(self):
        self.__menu = tk.Menu(self, tearoff=0)
        menu = tk.Menu(self, tearoff=0)
        for type in self.__component.get_types():
            menu.add_command(label=type, command=lambda: self.change_component_type(
                self.__component, type))
        self.__menu.add_cascade(
            label="Change statement type", menu=menu)

    def show_update_form(self):
        update_form = tk.Toplevel(self)
        current_components = self.__component.get_current_components()

        entries = self._create_entry_widgets(
            update_form, current_components)

        submit_button = self._create_submit_button(
            update_form, entries)
        submit_button.grid(row=len(current_components), column=0, columnspan=2)

        for (_, _, var) in entries:
            var.trace_add('write', lambda *args, button=submit_button,
                          vars_and_types=entries: self.update_button_state(button, entries))

    def _create_entry_widgets(self, update_form, current_components):
        entries = []

        for i, (entry_name, [entry_value, entry_type]) in enumerate(current_components.items()):
            entry_var = tk.StringVar()
            entries.append((entry_name, entry_type, entry_var))
            if (entry_type == ContractNonTerminal.DATE):
                custom_date_entry_var = tk.StringVar()
                entries.append((f"{entry_name}_custom",
                               ContractNonTerminal.DATE, custom_date_entry_var))
            self._create_entry_label(update_form, entry_name, i)
            self._create_entry_method(
                update_form, entry_var, entry_value, entry_type, i, entries)

        return entries

    def _create_submit_button(self, parent, entry_vars_and_types):
        submit_button = tk.Button(parent, text="Submit", command=lambda: self.update(
            entry_vars_and_types, parent))
        return submit_button

    def _create_entry_method(self, parent, entry_var, entry_value, entry_type, row, entries):
        match entry_type:
            case ContractNonTerminal.HOLDS | ContractNonTerminal.VERB | ContractNonTerminal.MODAL_VERB:
                return self._create_option_widget(parent, entry_var, entry_value, entry_type, row)
            case ContractNonTerminal.DATE:
                return self._create_date_widgets(parent, entry_var, entry_value, row, entries[-1][2])
            case _:
                return self._create_entry_widget(parent, entry_var, entry_value, row)

    def _create_entry_label(self, parent, text, row):
        entry_label = tk.Label(parent, text=f"{text}:")
        entry_label.grid(row=row, column=0)

    def _create_entry_widget(self, parent, entry_var, entry_value, row):
        entry_widget = tk.Entry(parent, textvariable=entry_var)
        entry_widget.insert(0, entry_value)
        entry_widget.grid(row=row, column=1)
        return entry_widget

    def _create_option_widget(self, parent, entry_var, entry_value, entry_type, row):
        options = ContractNonTerminal.get_options(entry_type)
        entry_var.set(entry_value)
        option_widget = tk.OptionMenu(parent, entry_var, *options)
        option_widget.grid(row=row, column=1)
        return option_widget

    def _create_date_widgets(self, parent, entry_var, entry_value, row, custom_var):
        options = ContractNonTerminal.get_options(ContractNonTerminal.DATE)

        date_widget = tk.OptionMenu(parent, entry_var, *options)
        date_widget.grid(row=row, column=1)

        custom_entry = tk.Entry(parent, textvariable=custom_var)
        custom_entry.grid(row=row, column=2)

        def handle_option_change(event):
            selected_option = entry_var.get()
            if selected_option == "custom date":
                custom_entry.grid(row=row, column=2)
            else:
                custom_entry.grid_forget()

        date_widget.bind("<Configure>", handle_option_change)

        return date_widget

    def update_button_state(self, button, entry_vars_and_types):
        button['state'] = 'normal' if all(ContractNonTerminal.validate_entry(var.get(
        ), entry_type) for _, (_, entry_type, var) in enumerate(entry_vars_and_types)) else 'disabled'

    def update(self, entries, update_form):
        update_dict = dict()
        date_dict = defaultdict(lambda: ("", ""))
        for entry_name, entry_type, entry_var in entries:
            if (entry_type == ContractNonTerminal.DATE):
                self._handle_date(entry_name, entry_var, date_dict)
            else:
                update_dict[entry_name] = entry_var.get()
        for date_name, date in date_dict.items():
            update_dict[date_name] = date
        Controller.update_component(self.__component, update_dict)
        self.trigger_re_render()
        update_form.destroy()

    @staticmethod
    def _handle_date(entry_name, entry_var, date_dict):
        if (entry_name.endswith("_custom")):
            date_entry = entry_name[:-7]
            current_date_value = date_dict[date_entry]
            date_dict[date_entry] = (current_date_value[0], entry_var.get())
        else:
            current_date_value = date_dict[entry_name]
            date_dict[entry_name] = (
                entry_var.get(), current_date_value[1])
