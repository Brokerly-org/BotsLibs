from datetime import datetime

from .widget import Widget


class DatePicker(Widget):
    ty = "date_picker"

    def __init__(self, initial: datetime, first: datetime, last: datetime, format: str = "yy-MM-dd"):
        self.initial = initial
        self.first = first
        self.last = last
        self.format = format

    def to_widget(self):
        return {
            "type": self.ty,
            "args": {
                "initial": self.initial.isoformat(),
                "first": self.first.isoformat(),
                "last": self.last.isoformat(),
                "format": self.format,
            }
        }
