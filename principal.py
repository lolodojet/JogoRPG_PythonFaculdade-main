from personagem import Personagem
from guerreiro import Guerreiro
from arqueiro import Arqueiro

nomeGuerreiro = input("Informe o seu nome: ")
guerreiro1 = Guerreiro (
    nome = nomeGuerreiro,
    classe = "Guerreiro",
    nivel = 1,
    vida = 100,
    forca = 0,
    dano = 0,
    tipoDeArma = "Espada",
    armadura = "Encantada"
    )
print(f"{guerreiro1.nome} Você é um Guerreiro!")
tuplaGuerreiro = ("Habilidades: Espada Fortificada", "| Armadura Encantada")
print(*tuplaGuerreiro)
guerreiro1.desenharPersonagem()
print()

arqueiro1 = Arqueiro(
    nome = "Garen",
    classe = "Arqueiro",
    nivel = 1,
    vida = 100,
    forca = 0,
    dano = 0,
    precisao = 100,
    flechaEspecial = "Flecha Flamejante"
)
print()
print("Seu inimigo é Garen um arqueiro mágico!")
tuplaArqueiro = ("Habilidades: Flecha Flamejante", "| Precisão 100%")
print(*tuplaArqueiro)
print()
arqueiro1.desenharPersonagem()
print()

jogoLigado = True
ataqueInicial = True

while jogoLigado:
    if guerreiro1.vida <= 0:
        print()
        print(f"(╥__╥) Você morreu!")
        print()
        print("FIM DE JOGO")
        
        escolhaContinuar = int(input("Quer jogar de novo? 1 - SIM | 2 - NÃO: "))
        if escolhaContinuar == 1:
            guerreiro1.vida = 100
            guerreiro1.forca = 0
            guerreiro1.nivel = 1
            arqueiro1.vida = 100
            arqueiro1.forca = 0
            arqueiro1.nivel = 1
            ataqueInicial = True
            continue
        else:
            print("Jogo encerrado!")
            jogoLigado = False
            continue
        
    elif arqueiro1.vida <= 0:
        print(f"O arqueiro foi derrotado.")
        print()
        print("\o/ Você venceu!")
        print("FIM DE JOGO")
        escolhaContinuar = int(input("Quer jogar de novo? 1 - SIM | 2 - NÃO: "))
        if escolhaContinuar == 1:
            guerreiro1.vida = 100
            guerreiro1.forca = 0
            guerreiro1.nivel = 1
            arqueiro1.vida = 100
            arqueiro1.forca = 0
            arqueiro1.nivel = 1
            ataqueInicial = True
            continue
        else:
            print("Jogo encerrado!")
            jogoLigado = False
            continue
    
    if ataqueInicial:
        print("== A GUERRA COMEÇOU ==")
        arqueiro1.dano = 10
        arqueiro1.atacar()
        guerreiro1.receberDano(arqueiro1.dano)
        ataqueInicial = False

    print("------------------------")
    print("=> Menu <=")
    print("1 - Contra Atacar")
    print("2 - Revide o ataque especial de Garen, use sua ultimate!")
    print("3 - Ver status")
    print("4 - Jogar de novo?")
    print("5 - Sair")
    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas os números válidos do menu!")
        continue
    
    if escolha < 1 or escolha > 5:
        print("Opção inválida! Digite um número entre 1 e 5.")
        continue

    print()
    if escolha == 1:
        
      # Digo quanto de dano meu guerreiro vai causar
        print(" CONTRA ATAQUE ") 
        print()
        guerreiro1.dano = 8 
        guerreiro1.atacar()
        arqueiro1.receberDano(guerreiro1.dano)
        print()
        arqueiro1.dano = 18
        print("Garen usou a ultimate para te atacar!")
        arqueiro1.usarHabilidadeEspecial()
        guerreiro1.receberDano(arqueiro1.dano)
    
    elif escolha == 2:
        print(" FORÇA MÁXIMA ")
        print()
        guerreiro1.usarHabilidadeEspecial()
        guerreiro1.dano = 15
        arqueiro1.receberDano(guerreiro1.dano)
        print()
        guerreiro1.subirNivel()
        
    elif escolha == 3:
        print("Seu status")
        guerreiro1.mostrarStatus()
        print()
        print("Status Arqueiro")
        arqueiro1.mostrarStatus()
        
    elif escolha == 4:
        while True:
            print()
            print("1 - SIM")
            print("2 - NÃO")
            print()
            try:
                escolhaContinuar = int(input("Escolha uma opção: "))
            except ValueError:
                print("Digite apenas números válidos (1 ou 2)!")
                continue
            
            if escolhaContinuar == 1:
                guerreiro1.vida = 100
                guerreiro1.forca = 0
                guerreiro1.nivel = 1
                arqueiro1.vida = 100
                arqueiro1.forca = 0
                arqueiro1.nivel = 1
                print()
                print("Jogo reiniciado! Os personagens foram resetados.")
                print()
                ataqueInicial = True
                break
            elif escolhaContinuar == 2:
                print("Jogo encerrado!")
                jogoLigado = False
                break
            else:
                print("\nOpção inválida! Digite 1 para SIM ou 2 para NÃO.")

            
    elif escolha == 5:
        while True:
            try:
                escolhaContinuar = int(input("\nQuer sair do jogo? \n1 - SIM  \n2 - NÃO \n"))
            except ValueError:
                print("Digite apenas números válidos (1 ou 2)!")
                continue
            
            if escolhaContinuar == 1:
                print("\nTCHAU GUERREIRO!")
                print("\nJogo encerrado.")
                jogoLigado = False
                break
            elif escolhaContinuar == 2:
                print("\nContinuando o jogo!")
                break
            else:
                print("\nOpção inválida! Digite 1 para SIM ou 2 para NÃO.")

