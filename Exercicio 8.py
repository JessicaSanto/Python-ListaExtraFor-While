#Escreva um programa que solicite ao usuário que insira números até que ele insira o número 0. Em seguida, imprima a soma de todos os números inseridos.

soma = 0  # Inicializa a variável soma como 0 para acumular os números inseridos

numero = float(input("Por favor, insira um número (ou 0 para sair): "))  # Solicita ao usuário que insira um número e o converte para ponto flutuante, armazenando-o na variável numero

while numero != 0:  # Inicia um loop while que continuará enquanto o número inserido for diferente de zero
    soma += numero  # Adiciona o número inserido à soma
    numero = float(input("Por favor, insira um número (ou 0 para sair): "))  # Solicita ao usuário que insira outro número e o converte para ponto flutuante, atualizando a variável numero

print("A soma de todos os números inseridos é:", soma)  # Imprime a soma de todos os números inseridos
