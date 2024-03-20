#Escreva um programa que solicite ao usuário que insira uma senha. O programa deve continuar solicitando a senha até que o usuário insira a senha correta.

senha_correta = "senha123"  # Define a senha correta como uma string
senha_digitada = input("Por favor, insira a senha: ")  # Solicita ao usuário que insira a senha e armazena-a na variável senha_digitada

while senha_digitada != senha_correta:  # Inicia um loop while que continuará enquanto a senha digitada não for igual à senha correta
    print("Senha incorreta. Tente novamente.")  # Se a senha estiver incorreta, imprime uma mensagem de erro
    senha_digitada = input("Por favor, insira a senha: ")  # Solicita ao usuário que insira a senha novamente e armazena-a em senha_digitada

print("Senha correta! Acesso concedido.")  # Quando a senha estiver correta, imprime uma mensagem de sucesso
