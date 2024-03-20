#Escreva um programa que solicite ao usuário que insira um número e, em seguida, imprima todos os números de 1 até esse número.

numero = int(input("Por favor, insira um número: "))  # Solicita ao usuário um número inteiro e o converte para o tipo int
contador = 1  # Inicializa uma variável contador com o valor 1

while contador <= numero:  # Inicia um loop while que continuará enquanto o contador for menor ou igual ao número inserido
    print(contador)  # Imprime o valor atual do contador
    contador += 1  # Incrementa o valor do contador em 1 a cada iteração do loop
