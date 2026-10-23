from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app=Flask(__name__)

def get_db_cannection():
    """ abre a conexão com o banco de dados SQLite local. """
    conn= sqlite3.connect('loja_roupas.db')
    return conn

def init_db():
    """ cria a tebela 'roupas' automaticamente no banco de dados se ela não existir """
    conn=get_db_cannection()
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTIS roupas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXTE NOT NULL,
            tamanho TEXT NOT NUL
        );
    ''')
    conn.commit()#grava oque foi gravado( escrito )
    conn.close()

    init_db()
@app.route('/')
def index():
    """rota princinpalmente: busca todas as roupas cadastradas e exibe no html """
    conn=get_db_cannection()
    cursor=conn.cursor()

    #consulta SQL para buscasr todos os registros
    cursor.execute('SELECT id , marca, tamanho FROM roupas ORDER BY id ASC;')
    roupas_cadastradas=cursor.fetchall()

    conn.close()

    return render_template('cadastro.html',roupas=roupas_cadastradas)

@app.route('/cadstrar', methods=['POST'])
def cadastra():
    """rota de cadastro:  recebe os dados digitados na tela e insere no banco de dados"""
    marca_digitada=request.form['marca']
    tamanho_digitado=request.form['tamanho']

    conn= get_db_cannection()
    cursor= conn.cursor()

    cursor.execute(
        'INSERT INTO roupas ( marca,tamanho) VALUES (?, ?);',
        (marca_digitada, tamanho_digitado)
    )

    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)


