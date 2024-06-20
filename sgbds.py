from sgbd_interface import  SGBD

class Paradox(SGBD):
    def conectar(self):
        print("Conectado ao Paradox SGBD")


class Firebird(SGBD):
    def conectar(self):
        print("Conectado ao Firebird SGBD")

class MySQL(SGBD):
    def conectar(self):
        print("Conectado ao MySQL SGBD")

        