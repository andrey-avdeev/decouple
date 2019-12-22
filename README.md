# Decouple
## Say NO to monolithic architecture.
Decouple complex system to separated modules by mediator.

```shell script
pip install decouple
```

## Register event handler
![register event handler](https://raw.githubusercontent.com/andrey-avdeev/decouple/master/docs/img/01_register.png)

## Dispatch events
![dispatch events](https://raw.githubusercontent.com/andrey-avdeev/decouple/master/docs/img/02_handle.png)

## Example
### Simple usage
Code of example is [here](https://github.com/andrey-avdeev/decouple/tree/master/examples/simple)

1. Write ModuleA - publisher
```python
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
```

2. Write ModuleB - subscriber
```python
from decouple import Module
from examples.simple.module_a import StartEvent


class ModuleB(Module):
    def __init__(self):
        super().__init__()

        self.sub(StartEvent, self.handle_a)

    def handle_start(self, event: StartEvent):
        print(f'field a:{event.a}')

```

3. Compose both modules to the whole
```python
from examples.simple.module_a import ModuleA
from examples.simple.module_b import ModuleB


module_a = ModuleA()
module_a.add(ModuleB())

module_a.start()
```

### Priorities
Manual control
```python
from decouple import Module
from examples.simple.module_a import StartEvent


class ModuleB(Module):
    def __init__(self):
        super().__init__()

        # handler with higher priority will be triggered early
        self.sub(StartEvent, self.handle_b, priority=0)
        self.sub(StartEvent, self.handle_a, priority=100)

    def handle_a(self, event: StartEvent):
        # will be triggered first
        print(f'field a:{event.a}')

    def handle_b(self, event: StartEvent):
        # will be triggered second
        print(f'event.uuid:{event.uuid}, event.timestamp:{event.timestamp}')
```
Default priority depends on registration order
```python
from decouple import Module
from examples.simple.module_a import StartEvent


class ModuleB(Module):
    def __init__(self):
        super().__init__()

        # priority of handlers call increased by 1 every registration for the same event
        self.sub(StartEvent, self.handle_b)   # priority=1
        self.sub(StartEvent, self.handle_a)   # priority=2

    def handle_a(self, event: StartEvent):
        # will be triggered second
        print(f'field a:{event.a}')

    def handle_b(self, event: StartEvent):
        # will be triggered first
        print(f'event.uuid:{event.uuid}, event.timestamp:{event.timestamp}')
```

# Feedback
I will be glad to read your feedback in issues and pull requests.