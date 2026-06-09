from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        print("usuario digitado", usuario)
        print("senha digitado", senha)

        cursor.execute(
            "SELECT * FROM usuario WHERE nome = ? AND senha = ?",
            (usuario, senha)
        )

        resultado = cursor.fetchone()

        conexao.close()

        if resultado:
            return "Login realizado com sucesso!"
        else:
            return "Usuário ou senha incorretos."

    return render_template("login.html")

app.run(debug=True)