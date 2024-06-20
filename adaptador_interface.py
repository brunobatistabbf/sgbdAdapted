from abc import ABC, abstractmethod
class Adaptador(ABC):
    def __init__(self, sgbd):
        self.sgbd = sgbd


    def conectar(self):
        pass