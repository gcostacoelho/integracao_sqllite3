from datetime import date
from sqlite3 import Error
def inserir(tabela, con):
    try:
        c = con.cursor()
        if tabela == 'tarefas':
            desc = input('Informe a tarefa: ').title()
            criado_em = date.today()
            tarefa = (desc, criado_em)
            c.execute("insert into tarefas (descricao, criado_em) values (?, ?);", tarefa)
            con.commit()
    except Error as e:
        print(e)
    else: print('Inserção com sucesso')

def atualizar(tabela, con):
    try:
        c = con.cursor()
        if tabela == 'tarefas':
            desc = input('Descrição: ').title()
            x = input('Informe o id da tarefa: ')
            tarefa = (desc, x)
            c.execute("update tarefas set descricao=? where idtarefas=?;", tarefa)
            con.commit()
    except Error as e:
        print(e)
    else: print('Atualização com sucesso')


def pesquisar(tabela, con):
    try:
        c = con.cursor()
        if tabela == 'tarefas':
            c.execute("select * from tarefas;")
        resultado = c.fetchall()
        if resultado:
            print("{:<5} {:<50} {:<10}".format('ID', 'DESCRIÇÃO', 'CRIADO_EM'))
            for i in range(len(resultado)):
                print("{:<5} {:<50} {:<10}".format(resultado[i][0], resultado[i][1], resultado[i][2]))
        else: print('Registro não encontrado')
    except Error as e:
        print(e)
    else: input('Pressione <ENTER> para continuar...')

def pesquisarUnico(tabela, con):
    try:
        c = con.cursor()
        if tabela == 'tarefas':
            descricao = input("Descrição: ").title()
            c.execute("SELECT * FROM tarefas WHERE descricao like (?);", ('%'+descricao+'%',))
            resultado = c.fetchall()
        if resultado:
            print("{:<5} {:<50} {:<10}".format("ID", "Descrição", "Criado_em"))
            for item in range(len(resultado)):
                print("{:<5} {:<50} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
        else:
            print(f"Não foram encontrados registros.")    
    except Error as e:
        print(e)
	
    input(f"Pressione <ENTER> para continuar ...")

def excluir(tabela, con):
	try:
		c = con.cursor()
		if tabela == 'tarefas':
			pesquisar(tabela, con)
			x = input("Informe o id da tarefa a excluir: ")
			tarefa = (x,)
			c.execute("DELETE FROM tarefas WHERE idtarefas=?;", tarefa)	
			con.commit()
	except Error as e:
		print(e)