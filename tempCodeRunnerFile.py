from flask import Flask
app = Flask(__name__)

# Importando as rotas 
from routes import *

if __name__ == "__main__":
    app.run()