from dataclasses import dataclass

from decouple import Module, Event, Mediator


class ModuleA(Module):
    def __init__(self, mediator: Mediator = Mediator()):
        super().__init__(mediator)

    def start(self):
        self.pub(StartEvent(a=7))


@dataclass
class StartEvent(Event):
    a: int = 0  # must be serializable
