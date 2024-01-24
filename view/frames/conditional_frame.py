import tkinter as tk

from view.constants import Constants
from view.frames.base_frame import BaseFrame
from view.frames.chain_frame import ChainFrame


class ConditionalFrame(BaseFrame):
    def __init__(self, parent, controller, re_render_func, conditional, **kwargs):
        super().__init__(
            parent,
            controller,
            re_render_func,
            conditional,
            {"multi-typed", "deletable", "hide_text"},
            **kwargs
        )
        self.__result = ChainFrame(
            parent, controller, re_render_func, self.get_component().get_result()
        )
        self.__condition = ChainFrame(
            parent, controller, re_render_func, self.get_component().get_condition()
        )

    def render(self, x, y):
        y += super().render(x, y)
        conditional_type = self.get_component().get_type().get_name()
        if conditional_type == "if":
            y = self.__result.render(x, y)
            y += self.create_text_and_get_height("IF", x, y)
            y = self.__condition.render(x, y)
            return y
        elif conditional_type == "if then":
            y += self.create_text_and_get_height("IF", x, y)
            y = self.__condition.render(x, y)
            y += self.create_text_and_get_height("THEN", x, y)
            y = self.__result.render(x, y)
            return y
        raise ValueError("Invalid conditional type")

    def create_text_and_get_height(self, text, x, y):
        parent = self.get_parent()
        label = tk.Message(parent, font=("Arial", 10), text=text, width=500)
        parent.create_window(x, y, anchor=tk.NW, window=label)
        parent.update()
        return label.winfo_reqheight()
