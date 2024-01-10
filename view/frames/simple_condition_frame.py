import tkinter as tk

from view.frames.base_frame import BaseFrame


class SimpleConditionFrame(BaseFrame):
    def __init__(self, parent, controller, condition, re_render_func, **kwargs):
        self.__condition = condition
        super().__init__(
            parent,
            controller,
            self.get_bg_colour(),
            self.get_button_text(),
            re_render_func,
            component=condition,
            **kwargs,
        )

    def create_widgets(self):
        button = tk.Button(self, text=self.get_text(), bg=self.get_bg_colour())
        button.grid(row=0, column=0, sticky=tk.W)
        self.add_type_submenu()
        self.add_chain_options()
        self.add_update_button()
        self.add_delete_button()
        button.bind("<Button-1>", self.show_menu)

    def destruct(self):
        self.get_controller().delete_non_definition_component(self.__condition.get_id())
        self.trigger_re_render()

    def get_bg_colour(self):
        return "teal"

    def get_button_text(self):
        match self.__condition.get_type():
            case "subject verb status":
                return "Subject verb status condition"
            case "subject date":
                return "Subject Date condition"
            case "date subject":
                return "Date Subject condition"
            case "subject modal verb":
                return "Date Subject condition"
            case "boolean expression":
                return "Boolean expression condition"
            case _:
                return "Unknown condition Type!"
