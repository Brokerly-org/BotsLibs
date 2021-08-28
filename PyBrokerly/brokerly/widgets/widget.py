from abc import ABC, abstractmethod


class Widget(ABC):

    @abstractmethod
    def to_widget(self):
        return NotImplemented
