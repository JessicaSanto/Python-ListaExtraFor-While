#Escreva um programa que solicite ao usuário que insira um número e, em seguida, imprima todos os números pares de 2 até esse número.

numero = int(input("Por favor, insira um número: "))  # Solicita ao usuário um número inteiro e o converte para o tipo int
contador = 2  # Inicializa uma variável contador com o valor 2

while contador <= numero:  # Inicia um loop while que continuará enquanto o contador for menor ou igual ao número inserido
    print(contador)  # Imprime o valor atual do contador
    contador += 2  # Incrementa o valor do contador em 2 a cada iteração do loop para garantir que apenas números pares sejam impressos
