class adaptador:
    def __init__(self, sgbd):
        self.sgbd = sgbd

    def conectar(self):
        self.sgbd.conectar()