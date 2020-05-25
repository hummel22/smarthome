from abc import ABC, abstractmethod
from typing import List

from smarthome.objects.sample import Sample


class Sensor(ABC):
    @abstractmethod
    def read(self) -> List[Sample]:
        raise NotImplementedError()
