from decouple import Module
from examples.simple.module_a import StartEvent


class ModuleB(Module):
    def __init__(self):
        super().__init__()

        self.sub(StartEvent, self.handle_start)

    def handle_start(self, event: StartEvent):
        print(f'field a:{event.a}')
