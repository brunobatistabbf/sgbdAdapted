from adaptador import AdaptadorParadox, AdaptadorFirebird, AdaptadorMySQL

class SelecionarSGBD:
    def __init__(self, perfil):
        self.perfil = perfil
        self.conexao = None
        self.selecionarConexao()

    def selecionarConexao(self):
        if self.perfil == 'Gratuito':
            self.conexao = AdaptadorParadox()
        elif self.perfil == "Básico":
            self.conexao = AdaptadorFirebird()
        elif self.perfil == "Ultimate":
            self.conexao = AdaptadorMySQL()
        else:
            print("SELECIONE UMA OPÇÃO VÁLIDA")

    def conectar(self):
        self.conexao.conectar()


if __name__ == '__main__':
    print("---------- SGBD CONNECTION --------")
    print("Escolha seu plano:")
    print("1 - Gratuito")
    print("2 - Básico")
    print("3 - Ultimate")
    print()
    perfil = int(input("Insira uma das opções"))














