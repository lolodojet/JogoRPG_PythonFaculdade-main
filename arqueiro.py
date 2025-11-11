from personagem import Personagem

class Arqueiro (Personagem):
    def __init__ (self, nome, classe, nivel, vida, forca, dano, precisao, flechaEspecial):
        super().__init__(nome, classe, nivel, vida, forca, dano)
        self.precisao = precisao
        self.flechaEspecial = flechaEspecial
        
    def atacar(self):
        print(f"{self.nome} atacou com a suas flechas flamejantes causando {self.dano} de dano")

    def receberDano(self, dano):
        self.vida -= dano
        if(self.vida < 0):
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano.\nVida atual de {self.nome}: {self.vida}")


    def usarHabilidadeEspecial(self):
        self.forca += 1
        
    def subirNivel(self):
        self.vida += 5
        if self.vida > 100:
            self.vida = 100
        self.forca += 1
        self.nivel += 1
        print(f"{self.nome} Subiu de nível! \nRecebeu: +{self.forca} de força, +{self.vida}. \nVocê agora está no nível {self.nivel}!")
    
    def mostrarStatus(self):
        print(f"Status - Nome: {self.nome} | Classe: {self.classe} | Nível: {self.nivel} | Vida: {self.vida} | Força: {self.forca}")

    def desenharPersonagem(self):
        
        print("    OOOO ")
        print("   O    O ")
        print("   O    O ")
        print("    OOOO ")
        print("   OOOOOOO ")
        print("  OO     OO   __")
        print(" O O     O O |  \\")
        print("O  O     O  O|   |")
        print("O  O     O   |   /")
        print("   O     O   |__/")
        print("   OOOOOOO ")
        print("   OO   OO ")
        print("   OO   OO ")
        print("   OO   OO ")
        print("   OO   OO ")
        