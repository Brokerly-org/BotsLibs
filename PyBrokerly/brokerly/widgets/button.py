from .widget import Widget


class Button(Widget):
    ty = "button"

    def __init__(self, text: str, data):
        self.text = text
        self.data = data

    def to_widget(self):
        return {"type": self.ty, "args": {"text": self.text, "data": self.data}}
