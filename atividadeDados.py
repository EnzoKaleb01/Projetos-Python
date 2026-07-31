import sqlite3

conexao = sqlite3.connect('exemplo.dB')

curso = conexao.cursor()

curso.execute('''
CREATE TABLE Alunos (
       ID INTEGER PRIMARY KEY,
       Nome TEXT NOT NULL,
       Idade INTEGER,
       Curso TEXT
)
''')

conexao.commit()

curso.execute('''
INSERT INTRO Alunos (Nome, Idade, Curso
VALUES ('Bruno', 24, 'Programador'),
       ('Kaleb', 29, 'medico'),
       ('Ana', 22, 'Vendedor'),
''')

conexao.commit()

nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
curso = input ("Qual seu curso: ")
inserir_dados(nome, idade, curso)