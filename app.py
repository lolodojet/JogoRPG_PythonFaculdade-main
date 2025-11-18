from flask import Flask, render_template, request, session, url_for, redirect
from guerreiro import Guerreiro
from arqueiro import Arqueiro

app = Flask(__name__)
app.secret_key = "chaveJogo_iniciar"

@app.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        session["nome"] = nome
        session["email"] = email

        guerreiro1 = Guerreiro (
        nome = nome,
        classe = "Guerreiro",
        nivel = 1,
        vida = 100,
        forca = 0,
        dano = 0,
        tipoDeArma = "Espada",
        armadura = "Encantada"
    )
        
        arqueiro1 = Arqueiro(
        nome="Garen",
        classe="Arqueiro",
        nivel=1,
        vida=100,
        forca=0,
        dano=0,
        precisao=100,
        flechaEspecial="Flecha Flamejante"
    )
         # Salva ambos na sessão como dicionário
        session["guerreiro"] = guerreiro1.__dict__
        session["arqueiro"] = arqueiro1.__dict__

        return render_template("cadastro.html", mensagem = f"Olá {guerreiro1.nome}, cadastrado com sucesso!")
    return render_template("cadastro.html", mensagem = "")


@app.route("/jogo", methods = ["GET", "POST"])
def inicioJogo():

    Guerreiro = session.get("guerreiro")
    Arqueiro = session.get("arqueiro")
    mensagem = ""

    if not Guerreiro or not Arqueiro:
        return redirect(url_for("/"))

    if request.method == "POST":
        acao = request.form["acao"]

        # Ataque
        if acao == "1":
            Guerreiro["dano"] = 8
            Arqueiro["vida"] -= Guerreiro["dano"]
            Arqueiro["dano"] = 18
            Guerreiro["vida"] -= Arqueiro["dano"]
            mensagem = f"{Guerreiro['nome']} atacou o arqueiro causando 8 de dano! Garen contra-atacou e causou 18 de dano."

        # ULTIMATE
        elif acao == "2":
            Guerreiro["dano"] = 15
            Arqueiro["vida"] -= Guerreiro["dano"]
            Arqueiro["dano"] = 10
            Guerreiro["vida"] -= Arqueiro["dano"]
            mensagem = f"{Guerreiro['nome']} usou um ataque especial causando 15 de dano! Garen contra-atacou e causou 10 de dano."

        # VER STATUS
        elif acao == "3":
            mensagem = f"{Guerreiro['nome']} - Vida: {Guerreiro['vida']} | Força {Guerreiro['forca']}, Nível {Guerreiro['nivel']}\n"
            
        # REINICIANDO JOGO
        elif acao == "4":
            Guerreiro["vida"] = 100
            Guerreiro["forca"] = 0
            Guerreiro["nivel"] = 1
            Arqueiro["vida"] = 100
            Arqueiro["forca"] = 0
            Arqueiro["nivel"] = 1
            mensagem = "Jogo reiniciado! Personagens resetados."

        # SAIR DO JOGO
        elif acao == "5":
            mensagem = "Obrigado(a) por jogar! Você saiu do jogo."
            return redirect(url_for("cadastro"))
        
        # VERIFICA FIM DO JOGO

        if Guerreiro["vida"] <= 0:
            mensagem += f" Você morreu! FIM DE JOGO."

        elif Arqueiro["vida"] <= 0:
            mensagem += f" Você venceu! FIM DE JOGO."


        session["guerreiro"] = Guerreiro
        session["arqueiro"] = Arqueiro
    

    return render_template("jogo.html", Guerreiro=Guerreiro, Arqueiro=Arqueiro, mensagem=mensagem)


@app.route("/blog")
def blog():
    return "Bem-vindo ao blog!"

if __name__ == "__main__":
    app.run(debug= True)