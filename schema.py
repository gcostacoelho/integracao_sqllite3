import sqlite3
from sqlite3 import Error

def criar_tabelas(bd):
    con = sqlite3.connect(bd)
    c = con.cursor()
    try:
        c.execute("""
                CREATE TABLE IF NOT EXISTS tarefas (
                        idtarefas INTEGER primary key,
                        descricao TEXT NOT NULL,
                        criado_em DATE NOT NULL);
                    """)
        return print('Tabelas criadas com sucesso')
    except Error as e: print(e)

