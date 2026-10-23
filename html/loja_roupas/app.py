from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    """Abre a conexão com o banco de dados SQLite local."""
    conn = sqlite3.connect('sistema_eventos.db')
    return conn

def init_db():
    """Cria a tabela 'roupas' automaticamente no banco de dados se ela ainda não existir."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eventos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            local TEXT NOT NULL,
            data INTEGER NOT NULL,
            capacidade INTEGER NOT NULL);
            ''')
    conn.commit()
    conn.close()

# Executa a inicialização da tabela ao rodar o aplicativo
init_db()

@app.route('/')
def index():
    """Rota principal: Busca todas as roupas cadastradas e exibe no HTML."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Consulta SQL para buscar todos os registros
    cursor.execute('SELECT id, nome, local, data, capacidade FROM eventos ORDER BY id ASC;')
    eventos_cadastrados = cursor.fetchall()
    
    conn.close()
    
    return render_template('evento.html', eventos=eventos_cadastrados)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    """Rota de cadastro: Recebe os dados digitados na tela e insere no banco."""
    nome_digitado = request.form['nome']
    local_digitado = request.form['local']
    data_digitada = request.form['data']
    capacidade_digitada = request.form['capacidade']
    
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Comando SQL para inserir novo registro
    cursor.execute(
        'INSERT INTO eventos (nome, local, data, capacidade) VALUES (?, ?, ?, ?);',
        (nome_digitado, local_digitado, data_digitada, capacidade_digitada)
    )
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '_main_':
    app.run(debug=True)