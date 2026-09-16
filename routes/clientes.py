from flask import Blueprint, request, jsonify, render_template, redirect, session
import sqlite3
from routes.auth import login_obrigatorio

clientes_bp = Blueprint('clientes', __name__)


@clientes_bp.route('/clientes', methods=['GET'])
@login_obrigatorio
def listar_clientes():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    clientes = conn.execute(
        'SELECT * FROM clientes WHERE usuario_id = ?',
        (session['usuario_id'],)
    ).fetchall()
    conn.close()

    return render_template('clientes.html', clientes=clientes)


@clientes_bp.route('/clientes', methods=['POST'])
@login_obrigatorio
def criar_clientes():
    nome = request.form['nome'].strip()
    telefone = request.form['telefone'].strip()
    email = request.form['email'].strip()

    if not nome or not telefone or not email:
        return "Todos os campos são obrigatórios", 400
    
    conn = sqlite3.connect('banco.db')
    conn.execute(
        'INSERT INTO clientes (nome, telefone, email, usuario_id) VALUES (?, ?, ?, ?)',
        (nome, telefone, email, session['usuario_id'])
    )
    conn.commit()
    conn.close()

    return redirect('/clientes')


@clientes_bp.route('/clientes/<int:id>/editar', methods=['GET'])
@login_obrigatorio
def form_editar_editar(id):
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    cliente = conn.execute(
        'SELECT * FROM clientes WHERE id = ? AND usuario_id = ?',
        (id, session['usuario_id'])
    ).fetchone()
    conn.close()

    return render_template('editar_cliente.html', cliente=cliente)


@clientes_bp.route('/clientes/<int:id>/editar', methods=['POST'])
@login_obrigatorio
def editar_clientes(id):
    nome = request.form['nome']
    telefone = request.form.get('telefone')
    email = request.form.get('email')

    conn = sqlite3.connect('banco.db')
    conn.execute(
        'UPDATE clientes SET nome = ?, telefone = ?, email = ? WHERE id = ? AND usuario_id = ?',
        (nome, telefone, email, id, session['usuario_id'])
    )
    conn.commit()
    conn.close()

    return redirect('/clientes')


@clientes_bp.route('/clientes/<int:id>/excluir', methods=['POST'])
@login_obrigatorio
def excluir_clientes(id):
    conn = sqlite3.connect('banco.db')
    conn.execute(
        'DELETE FROM clientes WHERE id = ? AND usuario_id = ?',
        (id, session['usuario_id'])
    )
    conn.commit()
    conn.close()

    return redirect('/clientes')