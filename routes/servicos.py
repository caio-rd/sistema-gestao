from flask import Blueprint, request, render_template, redirect, session
from routes.auth import login_obrigatorio
import sqlite3

servicos_bp = Blueprint("servicos", __name__)

@servicos_bp.route('/servicos', methods=['GET'])
@login_obrigatorio
def listar_servicos():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    servicos = conn.execute("""
        SELECT servicos.id, servicos.descricao, servicos.valor, clientes.nome AS clientes_nome
        FROM servicos
        JOIN clientes ON servicos.cliente_id = clientes.id
        WHERE clientes.usuario_id = ?
    """, (session['usuario_id'],)).fetchall()

    clientes = conn.execute(
        'SELECT * FROM clientes WHERE usuario_id = ?',
        (session['usuario_id'],)
    ).fetchall()
    conn.close()

    return render_template('servicos.html', servicos=servicos, clientes=clientes)


@servicos_bp.route('/servicos', methods=['POST'])
@login_obrigatorio
def criar_servico():
    descricao = request.form['descricao']
    valor = request.form['valor']
    cliente_id = request.form['cliente_id']

    if not descricao or not valor:
        return "Todos os campos são obrigatórios", 400

    conn = sqlite3.connect('banco.db')

    cliente_valido = conn.execute(
        'SELECT id FROM clientes WHERE id = ? AND usuario_id = ?',
        (cliente_id, session['usuario_id'])
    ).fetchone()

    if not cliente_valido:
        conn.close()
        return "Cliente inválido", 403

    conn.execute(
        'INSERT INTO servicos (descricao, valor, cliente_id) VALUES (?, ?, ?)',
        (descricao, valor, cliente_id)
    )
    conn.commit()
    conn.close()

    return redirect('/servicos')

@servicos_bp.route('/servicos/<int:id>/editar', methods=['GET'])
@login_obrigatorio
def form_editar_editar(id):
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    servicos = conn.execute("""
        SELECT servicos.*
        FROM servicos
        JOIN clientes ON servicos.cliente_id = clientes.id
        WHERE servicos.id = ? AND clientes.usuario_id = ?
    """, (id, session['usuario_id'])).fetchone()
    conn.close()

    return render_template('editar_servicos.html', servicos=servicos)

@servicos_bp.route('/servicos/<int:id>/editar', methods=['POST'])
@login_obrigatorio
def editar_servicos(id):
    descricao = request.form['descricao']
    valor = request.form.get('valor')

    conn = sqlite3.connect('banco.db')
    conn.execute("""
        UPDATE servicos SET descricao = ?, valor = ?
        WHERE id = ? AND cliente_id IN (
            SELECT id FROM clientes WHERE usuario_id = ?
        )
    """, (descricao, valor, id, session['usuario_id']))
    conn.commit()
    conn.close()

    return redirect('/servicos')

@servicos_bp.route('/servicos/<int:id>/excluir', methods=['POST'])
@login_obrigatorio
def excluir_servicos(id):
    conn = sqlite3.connect('banco.db')
    conn.execute("""
        DELETE FROM servicos
        WHERE id = ? AND cliente_id IN (
            SELECT id FROM clientes WHERE usuario_id = ?
        )
    """, (id, session['usuario_id']))
    conn.commit()
    conn.close()

    return redirect('/servicos')