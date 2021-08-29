from .widget import Widget


class Switch(Widget):
    ty = "switch"

    def __init__(self, initial_status: bool):
        self.initial = initial_status

    def to_widget(self):
        return {"type": self.ty, "args": {"initial": self.initial}}
