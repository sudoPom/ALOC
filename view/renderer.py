from view.constants import Constants
from view.frames import (base_frame, chain_frame, conditional_frame,
                         contract_frame)


class Renderer:
    def __init__(self, frame, controller, re_render_func):
        self.__frame = frame.get_canvas()
        self.__controller = controller
        self.__re_render_func = re_render_func

    def render(self, x, y, contract):
        self.__frame.delete("all")
        y += contract_frame.ContractFrame(
            self.__frame, self.__controller, self.__re_render_func
        ).render(x, y)
        x += Constants.INDENT_SIZE_PX
        for component_collection in contract.get_component_collections():
            components = component_collection.get_components()
            for component in components:
                y = self.render_component(x, y, component)

    def render_component(self, x, y, component):
        match component.get_component_type():
            case "simple_component":
                y = base_frame.BaseFrame(
                    self.__frame,
                    self.__controller,
                    self.__re_render_func,
                    component,
                    {"updatable", "deletable", "multi-typed"},
                ).render(x, y)
            case "base_chain":
                print(x)
                y = chain_frame.ChainFrame(
                    self.__frame,
                    self.__controller,
                    self.__re_render_func,
                    component,
                ).render(x, y)
            case "conditional":
                print(x)
                y = conditional_frame.ConditionalFrame(
                    self.__frame, self.__controller, self.__re_render_func, component
                ).render(x, y)
        return y


"""
    def render_contract(self, x, y, contract):
        self.__frame.delete("all")
        contract_frame_widget = contract_frame.ContractFrame(
            self.__frame, self.__controller, self.__re_render_func
        )

        self.__frame.create_window(x, y, anchor=tk.NW, window=contract_frame_widget)
        self.__frame.update()
        y += contract_frame_widget.winfo_reqheight()

        for definition in contract.get_definitions():
            y += PADDING_PX
            y += self.render_definition(definition, x + INDENT_SIZE_PX, y)

        for component in contract.get_other_components():
            y += PADDING_PX
            if isinstance(component, SimpleStatement):
                y = self.render_statement(component, x + INDENT_SIZE_PX, y)
            elif isinstance(component, ConditionalStatement):
                y = self.render_conditional_statement(component, x + INDENT_SIZE_PX, y)
            elif isinstance(component, ConditionalDefinition):
                y = self.render_conditional_definition(component, x + INDENT_SIZE_PX, y)

    def render_definition(self, definition, x, y):
        definition_frame_widget = simple_definition_frame.SimpleDefinitionFrame(
            self.__frame, self.__controller, definition, self.__re_render_func
        )
        return self.create_window_and_get_height(
            definition_frame_widget, x, y, definition.get_display_text()
        )

    def render_statement(self, statement, x, y):
        current_statement = statement
        while current_statement:
            statement_frame_widget = simple_statement_frame.SimpleStatementFrame(
                self.__frame,
                self.__controller,
                current_statement,
                self.__re_render_func,
            )
            y += self.create_window_and_get_height(
                statement_frame_widget, x, y, current_statement.get_display_text()
            )
            current_statement = current_statement.get_next_component()
        return y

    def render_condition(self, condition, x, y):
        current_condition = condition
        while current_condition:
            condition_frame_widget = simple_condition_frame.SimpleConditionFrame(
                self.__frame,
                self.__controller,
                current_condition,
                self.__re_render_func,
            )
            y += self.create_window_and_get_height(
                condition_frame_widget, x, y, current_condition.get_display_text()
            )
            current_condition = current_condition.get_next_component()
        return y

    def render_conditional_statement(self, conditional_statement, x, y):
        conditional = conditional_statement.get_condition()
        statement = conditional_statement.get_statement()
        conditional_statement_widget = (
            conditional_statement_frame.ConditionalStatementFrame(
                self.__frame,
                self.__controller,
                conditional_statement,
                self.__re_render_func,
            )
        )
        y += self.create_window_and_get_height(conditional_statement_widget, x, y)
        if conditional_statement.get_type() == "if":
            return self._render_if_conditional(
                statement,
                conditional,
                x + INDENT_SIZE_PX,
                y,
            )
        return self._render_if_then_conditional(
            statement,
            conditional,
            x + INDENT_SIZE_PX,
            y,
        )

    def render_conditional_definition(self, conditional_definition, x, y):
        conditional = conditional_definition.get_condition()
        definition = conditional_definition.get_definition()
        conditional_definition_widget = (
            conditional_definition_frame.ConditionalDefinitionFrame(
                self.__frame,
                self.__controller,
                conditional_definition,
                self.__re_render_func,
            )
        )
        y += self.create_window_and_get_height(conditional_definition_widget, x, y)
        if conditional_definition.get_type() == "if":
            return self._render_if_conditional(
                definition,
                conditional,
                x + INDENT_SIZE_PX,
                y,
            )
        return self._render_if_then_conditional(
            definition,
            conditional,
            x + INDENT_SIZE_PX,
            y,
        )

    def _render_if_conditional(self, component, condition, x, y):
        if isinstance(component, SimpleDefinition):
            y += self.render_definition(component, x, y)
        else:
            y = self.render_statement(component, x, y)
        y += self.create_text_and_get_height("if", x, y)
        y = self.render_condition(condition, x, y)
        return y

    def _render_if_then_conditional(self, component, condition, x, y):
        y += self.create_text_and_get_height("if", x, y)
        y = self.render_condition(condition, x, y)
        y += self.create_text_and_get_height("then", x, y)
        if isinstance(component, SimpleDefinition):
            return y + self.render_definition(component, x, y)
        else:
            return self.render_statement(component, x, y)

    def create_text_and_get_height(self, text, x, y):
        label = tk.Message(self.__frame, font=("Arial", 10), text=text, width=500)
        self.__frame.create_window(x, y, anchor=tk.NW, window=label)
        self.__frame.update()
        return label.winfo_reqheight()

    def create_window_and_get_height(self, widget, x, y, display_text=None):
        self.__frame.create_window(x, y, anchor=tk.NW, window=widget)
        self.__frame.update()
        if not display_text:
            return widget.winfo_reqheight()
        label = tk.Message(widget, font=("Arial", 10), text=display_text, width=500)
        label.grid(row=1, column=0, sticky=tk.W)
        self.__frame.update()
        return widget.winfo_reqheight()
"""
