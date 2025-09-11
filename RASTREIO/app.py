from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

BANDO_DE_DADOS = "banco_rastreio.db"

def get_db():
    db = sqlite3.connect(BANDO_DE_DADOS)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/iniciar')
def iniciar():
    init_db()
    return 'Banco de dados iniciando...'

@app.route('/', methods=['GET'])
def index():
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT * FROM encomendas')
        dados = cur.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500 # < -- ERRO DE SERVIDOR!
    finally:
        db.close()