from flask import Flask
import sqlite3
from routes.auth import auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)

app.secret_key = "troque-isso-por-algo-aleatorio-depois"

from routes.clientes import clientes_bp
app.register_blueprint(clientes_bp)

from routes.servicos import servicos_bp
app.register_blueprint(servicos_bp)

from routes.dashboard import dashboard_bp
app.register_blueprint(dashboard_bp)

@app.route("/")
def inicio():
    return "Back-end funcionando!"


conn = sqlite3.connect("banco.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL,
        usuario_id INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
""")
conn.commit()
conn.close()

conn = sqlite3.connect('banco.db')
conn.execute("""

    CREATE TABLE IF NOT EXISTS servicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        cliente_id INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
""")

conn.commit()
conn.close()


conn = sqlite3.connect('banco.db')
conn.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL
    )
""")

conn.commit()
conn.close()




if __name__ == "__main__":
    app.run(debug=True)