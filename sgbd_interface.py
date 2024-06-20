from abc import ABC, abstractmethod

class SGBD(ABC):
    @abstractmethod
    def conectar(self):
        pass
