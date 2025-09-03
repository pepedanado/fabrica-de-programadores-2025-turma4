import sqlite3

con = sqlite3.connect("meu_banco.db")

try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor() # abrindo o cursor

    #cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)") # criando tabela pessoa

    #cur.execute("INSERT INTO pessoa VALUES(1, 'Pedro', 17, '535.793.788-XX')")

    res = cur.execute("SELECT * FROM pessoa")
    
    pessoas = res.fetchone()

    print(pessoas)

    con.commit()

except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')