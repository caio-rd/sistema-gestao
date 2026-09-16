from flask import Blueprint, request, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registrar", methods=["GET"])
def form_registrar():
    return render_template("registrar.html")

@auth_bp.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    senha_hash = generate_password_hash(senha)

    conn = sqlite3.connect('banco.db')
    conn.execute (
        'INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)',
        (nome, email, senha_hash)
    )

    conn.commit()
    conn.close()

    return redirect('/login')


@auth_bp.route("/login", methods=["GET"])
def form_login():
    return render_template("login.html")

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    usuario = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
    conn.close()

    if usuario and check_password_hash(usuario['senha_hash'], senha):
        session['usuario_id'] = usuario['id']
        return redirect('/clientes')
    return render_template('login.html', erro='Email ou senha incorretos'), 401

@auth_bp.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect('/login')

from functools import wraps

def login_obrigatorio(funcao):
    @wraps(funcao)
    def decorada(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect("/login")
        return funcao(*args, **kwargs)
    return decorada
