import psycopg2

# Estabelecendo a conexão com o Banco de dados
def conectardb():
    conexao = psycopg2.connect(database="minicursoDb",
                               host="localhost",
                               user="postgres",
                               password="1234",
                               port="5432")
    print("Conexão Realizada com sucesso!")
    return conexao

# Chame a função para testar a conexão
conexao = conectardb()

#inserir usuario
def inserir_usuario(nome, email):
    conexao = conectardb()
    curso = conexao.cursor()

    curso.execute("INSERT INTO usuarios(nome, email) VALUES (%s,%s)", (nome,email))

    conexao.commit()
    curso.close()
    conexao.close()

def deletar_usuario(id):
    conexao = conectardb()
    curso = conexao.cursor()

    curso.execute("DELETE FROM usuarios WHERE id = %s", (id,))

    conexao.commit()
    curso.close()
    conexao.close()