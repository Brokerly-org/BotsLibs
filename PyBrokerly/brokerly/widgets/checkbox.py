from .widget import Widget


class Checkbox(Widget):
    ty = "checkbox"

    def __init__(self, initial_status: bool):
        self.initial = initial_status

    def to_widget(self):
        return {
            "type": self.ty,
            "args": {"initial": self.initial}
        }
