import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'hope'
)
nome = "MKSN"
login = "klaus"
senha = "1000"

cursor = conexao.cursor()

#comando = "select * from hp_login"
comando = f'insert into hp_login(nome,login,senha) values("{nome}","{login}","{senha}")'
cursor.execute(comando)

#resultado = cursor.fetchall()
conexao.commit()
print("cadastrado")