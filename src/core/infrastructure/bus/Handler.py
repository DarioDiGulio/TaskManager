from abc import abstractmethod
from typing import Any


class Handler:
    name = 'Handler'

    @abstractmethod
    def execute(self, request: Any):
        pass
