# Definição de usuário e senha corretos
USUARIO_CORRETO = "Kaleb01"
SENHA_CORRETA = "1234"

# Solicita as credenciais do usuário
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verifica se as credenciais estão corretas
if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
    print("Login bem-sucedido! Bem-vindo ao sistema.")
else:
    print("Erro: Usuário ou senha incorretos. Tente novamente.")
