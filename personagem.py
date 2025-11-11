class Personagem:

    def __init__(self, nome, classe, nivel, vida, forca, dano):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.vida = vida
        self.forca = forca
        self._dano = 0 #  (atributo interno com underscore -> convenção para "privado").


    @property
    def dano (self):
        return self._dano
    @dano.setter
    def dano(self, valor):
        if valor < 0:
            raise ValueError("Dano não pode ser negativo")
        self._dano = valor


    def atacar(self):
        if (self.classe == "Arqueiro"):
            print(f"{self.nome} atirou com sua flecha, causando 10 de dano!")
        elif (self.classe == "Guerreiro"):
            print(f"{self.nome} atacou com a sua espada, causando 8 de dano!")


    def receberDano(self, dano):
        self.vida -= dano
        if (self.vida < 0):
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} foi atingido(a) e recebeu {dano} de dano.\nVida atual: {self.vida}")


    def usarHabilidadeEspecial(self):
        if self.classe == "Arqueiro":
            self.forca += 1
            print(f"{self.nome}  {self.classe} usou seu -Arco Ultimate- causando 18 de dano!")
        elif self.classe == "Guerreiro":
            print(f"{self.nome}  {self.classe} revidou atacando com as sua -Espada fortificada- causando 15 de dano. Força aumentada em 2!")


    def subirNivel(self):
        self.vida += 5
        if (self.vida > 100):
            self.vida = 100
        self.nivel += 1
        self.forca += 1
        
        print(f"{self.nome} Subiu de nível! \nRecebeu: +{self.forca} de força e +{self.vida} de vida. Agora você está nível {self.nivel}!")
   
    def mostrarStatus (self):
        print(f"Staus - Nome: {self.nome} | Classe: {self.classe} | Nivel: {self.nivel} | Vida: {self.vida} | Força: {self.forca}")
    
    def desenharPersonagem(self):

        if self.classe == "Arqueiro":
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
        
        elif self.classe == "Guerreiro":

            print("    OOOO ")
            print("   O    O ")
            print("   O    O ")
            print("    OOOO ")
            print("   OOOOOOO ")
            print("  OO     OO   |")
            print(" O O     O O  |")
            print("O  O     O  =O|==")
            print("O  O     O    |")
            print("   OOOOOOO")
            print("   OO   OO")
            print("   OO   OO")
            print("   OO   OO")
            print("   OO   OO")


