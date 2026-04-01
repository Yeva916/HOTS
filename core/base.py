from abc import ABC, abstractmethod
import processor
class BaseProcessor(ABC):
    @abstractmethod
    def process(self, payload):
        pass

