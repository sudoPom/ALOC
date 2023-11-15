from model.utils import extract_key, throw_if_no_keys_found


class BaseSimpleDefinition:
    def __init__(self, id):
        self.id = id
        self.subject = ""
        self.components = {"subject"}

    def update(self, **kwargs):
        throw_if_no_keys_found(kwargs, self.components)
        self.subject = extract_key(kwargs, "other_subject". this.subject)

    def get_id(self):
        return self.id

class SubjectSimpleDefinition(BaseSimpleDefinition):
    def __init__(self, id):
        super().__init__(id)
        self.other_subject = ""
        self.components.add("other_subject")

    def update(self, **kwargs):
        super().update(kwargs)
        throw_if_no_keys_found(kwargs, self.components)
        self.other_subject = extract_key(kwargs, "other_subject". this.other_subject)

    def render(self):
        return f"{subject} is {other_subject}."

class NumericalSimpleDefinition(BaseSimpleDefinition):
    def __init__(self, id):
        super().__init__(id)
        self.numerical_expression = None
        self.components.add("numerical_expression")
    
    def update(self, **kwargs):
        throw_if_no_keys_found(kwargs, self.components)
        self.numerical_expression = extract_key(kwargs, "other_subject". this.numerical_expression)

    def render(self):
        return f"{subject} equals {numerical_expression}"

