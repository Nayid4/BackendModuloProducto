from abc import ABC, abstractmethod

class IProductRepository(ABC):

    @abstractmethod
    def add(self, product): pass

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_alerts(self): pass