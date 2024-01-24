from view.frames.base_frame import BaseFrame


class ChainFrame(BaseFrame):
    def __init__(self, parent, controller, re_render_func, component):
        super().__init__(
            parent,
            controller,
            re_render_func,
            component,
            {"updatable", "deletable", "chain_component", "multi-typed"},
        )

    def render(self, x, y):
        current_component = self.get_component()
        y += super().render(x, y)
        current_component = current_component.get_next_component()
        while current_component:
            y += BaseFrame(
                self.get_parent(),
                self.get_controller(),
                self.get_re_render_func(),
                current_component,
                {"updatable", "multi-typed", "deletable", "chain_component"},
            ).render(x, y)
            current_component = current_component.get_next_component()
        return y
