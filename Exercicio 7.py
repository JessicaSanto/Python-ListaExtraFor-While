#Escreva um programa que calcule a média de uma lista de números fornecida pelo usuário.

quantidade = int(input("Quantos números você deseja inserir? "))  # Solicita ao usuário que insira a quantidade de números que deseja inserir e armazena o valor na variável quantidade

soma = 0  # Inicializa a variável soma como 0 para acumular os números inseridos
contador = 0  # Inicializa o contador como 0 para controlar quantos números foram inseridos até o momento

while contador < quantidade:  # Inicia um loop while que continuará enquanto o contador for menor que a quantidade desejada de números
    numero = float(input("Por favor, insira um número: "))  # Solicita ao usuário que insira um número e o converte para ponto flutuante, armazenando-o na variável numero
    soma += numero  # Adiciona o número inserido à soma
    contador += 1  # Incrementa o contador para acompanhar quantos números foram inseridos até o momento

media = soma / quantidade  # Calcula a média dos números inseridos dividindo a soma pela quantidade de números
print("A média dos números é:", media)  # Imprime a média dos números inseridos
