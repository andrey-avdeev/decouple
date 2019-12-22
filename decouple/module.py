from __future__ import annotations

from typing import Optional, Callable, Any, Union

from .mediator import Mediator
from .publisher import Publisher


class Module(Publisher):
    def __init__(self, mediator: Optional[Mediator] = None):
        super().__init__(mediator)
        self._lazy_subscriptions = []

    def sub(self, event: Union[type, str], handler: Callable[[Any], None]):
        if self._mediator:
            self._mediator.add(event, handler)
        else:
            self._lazy_subscriptions.append((event, handler))

        return self

    def init(self, mediator: Mediator):
        if not self._mediator:
            self._mediator = mediator
            if self._lazy_subscriptions:
                subscriptions = self._lazy_subscriptions
                self._lazy_subscriptions = []

                for event, handler in subscriptions:
                    self.sub(event, handler)

    def add(self, module: Module) -> Module:
        module.init(self._mediator)

        return self
