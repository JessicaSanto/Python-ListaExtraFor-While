#Escreva um programa que solicite ao usuário que insira um número e, em seguida, imprima a tabuada desse número até 10.

numero = int(input("Por favor, insira um número: "))  # Solicita ao usuário um número inteiro e o converte para o tipo int
contador = 1  # Inicializa uma variável contador com o valor 1

print("Tabuada de", numero, ":")  # Imprime o cabeçalho indicando a tabuada do número inserido

while contador <= 10:  # Inicia um loop while que continuará enquanto o contador for menor ou igual a 10
    resultado = numero * contador  # Calcula o resultado multiplicando o número inserido pelo contador atual
    print(numero, "x", contador, "=", resultado)  # Imprime a multiplicação na forma "número x contador = resultado"
    contador += 1  # Incrementa o contador para passar para o próximo número na tabuada
