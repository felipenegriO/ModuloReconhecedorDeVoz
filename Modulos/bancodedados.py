import MySQLdb

class BancoDeDados:

    conexao = None

    def __init__(self):
        global conexao
        try:
            db = MySQLdb.connect("localhost","acesso","@acesso@","proj_rec_voz")
            conexao=db.cursor()
        except:
            print "Erro ao tentar se conectar com o banco de dados"


    def exSql(self,sql):
        global conexao
	resultado =conexao.execute(sql)
        resultado.fetchall()
        return resultado
