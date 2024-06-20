from sgbds import Paradox, Firebird, MySQL
from adaptador_interface import adaptador

class AdaptadorParadox(adaptador):
    def __init__(self):
        super().__init__(Paradox())
        
class AdaptadorFirebird(adaptador):
    def __init__(self):
        super().__init__(Firebird())
        
class AdaptadorMySQL(adaptador):
    def __init__(self):
        super().__init__(MySQL())
    
        