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

    def menu_close(self):
        self.__menu.unpost()

    def show_menu(self):
        raise NotImplementedError(
            "Base class method for show_menu should be overridden")
