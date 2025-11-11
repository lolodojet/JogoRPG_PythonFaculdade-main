from main import app

@app.route("/")
def homepage():
    return "Bem-vindo à página inicial!"

@app.route("/blog")
def blog():
    return "Bem-vindo ao blog!"