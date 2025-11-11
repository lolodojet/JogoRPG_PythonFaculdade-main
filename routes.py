from main import app

# Renderiza um template (HTML)
from flask import render_template  


@app.route("/")
def homepage():
    return render_template("inicio.html")
    # Retornando o conteúdo do arquivo inicio.html

@app.route("/blog")
def blog():
    return "Bem-vindo ao blog!"