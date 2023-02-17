from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Handler(ABC):
    def __init__(self):
        self.next: Optional[Handler] = None

    def set_next(self, handler: Handler) -> None:
        self.next = handler

    def handle_click_event(self) -> None:
        try:
            if self.on_click() and self.next:
                self.next.handle_click_event()
        except AttributeError:
            pass

    @abstractmethod
    def on_click(self) -> bool:
        """Handle a click event."""


@dataclass
class Button(Handler):
    name: str = "button"
    activate: bool = True

    def on_click(self) -> bool:
        if self.activate:
            print(f"Button [{self.name}] handling click.")
            return True
        return False


@dataclass
class Panel(Handler):
    name: str = "panel"
    activate: bool = True

    def on_click(self) -> bool:
        if self.activate:
            print(f"Panel [{self.name}] handling click.")
            return True
        return False


@dataclass
class Window(Handler):
    name: str = "window"
    activate: bool = True
    def on_click(self) -> bool:
        if self.activate:
            print(f"Window [{self.name}] handling click.")
            return True
        return False


def main() -> None:
    button = Button(name="my_button", activate=True)
    panel = Panel(name="my_panel")
    window = Window(name="my_window")

    # setup the chain of responsibility
    button.set_next(panel)
    panel.set_next(window)

    button.handle_click_event()


if __name__ == "__main__":
    main()
