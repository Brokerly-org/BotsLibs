from .widget import Widget


class TimePicker(Widget):
    ty = "time_picker"

    def __init__(self, initial_hour: int, initial_minute: int):
        self.initial_hour = initial_hour
        self.initial_minute = initial_minute

    def to_widget(self):
        return {
            "type": self.ty,
            "args": {
                "initial_hour": self.initial_hour,
                "initial_minute": self.initial_minute,
            }
        }
