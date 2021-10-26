import sqlite3
from sqlite3 import Error
from time import sleep
import os
import schema
import tables

def criar_conexao(bd):
    con = None
    try: 
        con = sqlite3.connect(bd)
        print(sqlite3.sqlite_version)
        return con
    except Error as e:
        print(f'Ocorreu um erro ao conectar: {e}')        

def menu():
    print(25 * '*')
    print('***--Menu de opções--***')
    print(25 * '*')
    print('1. Manter tarefas')
    print('2. Sair do programa')
    print(25 * '*')
    selecao = int(input('Escolha uma opção: '))
    return selecao

def subMenu(tables):
    print(22 * '*')
    print(f'***--Opções {tables}--***')
    print(22 * '*')
    print('0. Retornar ao menu pricipal')
    print(f'1. Inserir {tables}')
    print(f'2. Atualizar {tables}')
    print(f'3. Pesquisar {tables}')
    print(f'4. Pesquisar único {tables}')
    print(f'5. Excluir {tables}')
    print(22 * '*')
    opcaoSub = int(input('Escolha uma opção: '))
    return opcaoSub


if __name__ == '__main__':
    os.system('clear')
    print(27 * '*')
    print('***--Projeto de exemplo--***')
    print(f'Criando banco de dados se não existir')
    
    banco = input('Informe o nome do banco a ser criado: ')
    print(f'Criando conexão com o banco de dados')
    con = criar_conexao(banco)
    
    print(f'Criando tabelas do banco de dados se não existirem')
    schema.criar_tabelas(banco)
    sleep(2)
    input('Pressione <ENTER> para continuar')
    
    os.system('clear')
    opcao = menu()
    os.system('clear')
    
    while opcao != 2:
        if opcao == 1: tabela = 'tarefas'
        else: print('Opção inválida')

        opcaoSub = subMenu(tabela)
        os.system('clear')
        while opcaoSub != 0:
            if opcaoSub == 1:
                tables.inserir(tabela, con)
            elif opcaoSub == 2:
                tables.atualizar(tabela, con)
            elif opcaoSub == 3:
                tables.pesquisar(tabela, con)
            elif opcaoSub == 4:
                tables.pesquisarUnico(tabela, con)
            elif opcaoSub == 5:
                tables.excluir(tabela, con)
            else: print('Opção inválida')
            
            os.system('clear')
            opcaoSub = subMenu(tabela)
            os.system('clear')
        
        opcao = menu()