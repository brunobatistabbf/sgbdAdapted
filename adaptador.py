from sgbds import Paradox, Firebird, MySQL
from adaptador_interface import Adaptador

class AdaptadorParadox(Adaptador):
    def __init__(self):
        super().__init__(Paradox())

    def conectar(self):
        self.sgbd.conectar()
class AdaptadorFirebird(Adaptador):
    def __init__(self):
        super().__init__(Firebird())

    def conectar(self):
        self.sgbd.conectar()
        
class AdaptadorMySQL(Adaptador):
    def __init__(self):
        super().__init__(MySQL())

    def conectar(self):
        self.sgbd.conectar()
    
        