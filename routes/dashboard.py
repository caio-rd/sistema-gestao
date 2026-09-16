from flask import Blueprint, render_template, session
from routes.auth import login_obrigatorio
import sqlite3

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
@login_obrigatorio
def dashboard():
    conn = sqlite3.connect("banco.db")
    conn.row_factory = sqlite3.Row

    total_clientes = conn.execute(
        "SELECT COUNT(*) AS total FROM clientes WHERE usuario_id = ?",
        (session['usuario_id'],)
    ).fetchone()["total"]

    total_servicos = conn.execute("""
        SELECT COUNT(*) AS total
        FROM servicos
        JOIN clientes ON servicos.cliente_id = clientes.id
        WHERE clientes.usuario_id = ?
    """, (session['usuario_id'],)).fetchone()["total"]

    valor_total = conn.execute("""
        SELECT SUM(servicos.valor) AS total
        FROM servicos
        JOIN clientes ON servicos.cliente_id = clientes.id
        WHERE clientes.usuario_id = ?
    """, (session['usuario_id'],)).fetchone()["total"] or 0

    detalhes = conn.execute("""
        SELECT clientes.nome AS cliente_nome, servicos.descricao, servicos.valor
        FROM servicos
        JOIN clientes ON servicos.cliente_id = clientes.id
        WHERE clientes.usuario_id = ?
        ORDER BY clientes.nome
    """, (session['usuario_id'],)).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_clientes=total_clientes,
        total_servicos=total_servicos,
        valor_total=valor_total,
        detalhes=detalhes
    )