from adaptador import AdaptadorParadox, AdaptadorFirebird, AdaptadorMySQL

class SelecionarSGBD:
    def __init__(self, perfil):
        self.perfil = perfil
        self.conexao = None
        self.selecionarConexao()

    def selecionarConexao(self):
        if self.perfil == "Gratuito":
            self.conexao = AdaptadorParadox()
        elif self.perfil == "Básico":
            self.conexao = AdaptadorFirebird()
        elif self.perfil == "Ultimate":
            self.conexao = AdaptadorMySQL()
        else:
            print("SELECIONE UMA OPÇÃO VÁLIDA")

    def conectar(self):
        if self.conexao:
            self.conexao.conectar()
        else:
            print("NÃO FOI POSSIVEL CONECTAR")

if __name__ == '__main__':
    print("---------- SGBD CONNECTION --------")
    print("Escolha seu plano:")
    print("1 - Gratuito")
    print("2 - Básico")
    print("3 - Ultimate")
    print()
    perfil_opcao = int(input("Insira uma das opções: "))

    if perfil_opcao == 1:
        perfil = "Gratuito"
        Cliente = SelecionarSGBD(perfil)
    elif perfil_opcao == 2:
        perfil = "Básico"
        Cliente = SelecionarSGBD(perfil)
    elif perfil_opcao == 3:
        perfil = "Ultimate"
        Cliente = SelecionarSGBD(perfil)
    else:
        print("ERRO - SELECIONE UMA OPÇÃO VÁLIDA")

    if Cliente:
        Cliente.conectar()











