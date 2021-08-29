from .widget import Widget


class Slider(Widget):
    ty = "slider"

    def __init__(
        self, initial_value: float, min: float, max: float, divisions: int = None
    ):
        self.initial = initial_value
        self.min = min
        self.max = max
        self.divisions = divisions

    def to_widget(self):
        return {
            "type": self.ty,
            "args": {
                "initial": self.initial,
                "min": self.min,
                "max": self.max,
                "divisions": self.divisions,
            },
        }
