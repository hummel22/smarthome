from abc import ABC, abstractmethod
from typing import List

from smarthome.objects.sample import Sample


class DB(ABC):
    @abstractmethod
    def write(self, data: List[Sample]):
        raise NotImplementedError()
