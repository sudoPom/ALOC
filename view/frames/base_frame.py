import tkinter as tk


class BaseFrame(tk.Frame):
    def __init__(self, parent, controller, colour, button_text, re_render_func, **kwargs):
        super().__init__(parent, **kwargs)
        self.__controller = controller
        self.__re_render_func = re_render_func
        self.__colour = colour
        self.__text = button_text
        self.__menu = None
        self.create_widgets()

    def get_text(self):
        return self.__text

    def get_colour(self):
        return self.__colour

    def get_controller(self):
        return self.__controller

    def trigger_re_render(self):
        self.__re_render_func()

    def create_widgets(self):
        raise NotImplementedError(
            "Base class method for create_widgets should be overridden")

    def show_menu(self):
        raise NotImplementedError(
            "Base class method for show_menu should be overridden")

    def show_update_form(self):
        update_form = tk.Toplevel(self)
        current_entries = self.get_entries()

        entry_vars_and_types = []
        entry_widgets = []

        for i, (entry_name, entry_value, entry_type) in enumerate(current_entries):
            entry_var = tk.StringVar()
            entry_vars_and_types.append((entry_var, entry_type))

            self.create_entry_label(update_form, entry_name, i)
            entry_widget = self.create_entry_widget(
                update_form, entry_var, entry_value, i)
            entry_widgets.append(entry_widget)

        submit_button = self.create_submit_button(
            update_form, entry_vars_and_types)
        submit_button.grid(row=len(current_entries), column=0, columnspan=2)

        for (var, _) in entry_vars_and_types:
            var.trace_add('write', lambda *args, btn=submit_button,
                          vars=entry_vars_and_types: self.update_button_state(btn, vars))

    @staticmethod
    def create_entry_label(parent, text, row):
        entry_label = tk.Label(parent, text=f"{text}:")
        entry_label.grid(row=row, column=0)

    @staticmethod
    def create_entry_widget(parent, entry_var, entry_value, row):
        entry_widget = tk.Entry(parent, textvariable=entry_var)
        entry_widget.insert(0, entry_value)
        entry_widget.grid(row=row, column=1)
        return entry_widget

    def create_submit_button(self, parent, entry_vars_and_types):
        submit_button = tk.Button(parent, text="Submit", command=lambda: self.update(
            [entry_var for (entry_var, entry_type) in entry_vars_and_types], parent))
        return submit_button

    def update(self, entries, update_form):
        raise NotImplementedError(
            "Base class method for update should be overridden")
