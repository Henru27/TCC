from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        return f"Usuário: {usuario} | Senha: {senha}"

    return render_template("index.html")

app.run(debug=True)