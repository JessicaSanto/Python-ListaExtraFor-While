#Escreva um programa que solicite ao usuário que insira números até que ele insira um número igual ao anterior. Em seguida, imprima quantos números ele inseriu.

contador = 0  # Inicializa o contador para contar o número de números únicos inseridos
anterior = None  # Inicializa a variável anterior para armazenar o número anterior inserido pelo usuário. None é usado para indicar que ainda não houve nenhum número inserido anteriormente.
numero = float(input("Por favor, insira um número (ou um número igual ao anterior para sair): "))  # Solicita ao usuário que insira um número e o converte para ponto flutuante, armazenando-o na variável numero

while numero != anterior:  # Inicia um loop while que continuará enquanto o número inserido for diferente do número anterior (ou seja, enquanto um número único for inserido)
    anterior = numero  # Atualiza o valor da variável anterior para o número inserido atualmente, para comparar com o próximo número inserido
    contador += 1  # Incrementa o contador para contar o número de números únicos inseridos
    numero = float(input("Por favor, insira um número (ou um número igual ao anterior para sair): "))  # Solicita ao usuário que insira outro número e o converte para ponto flutuante, atualizando a variável numero

print("Você inseriu", contador, "números.")  # Quando o usuário insere um número igual ao anterior ou decide sair, o loop é interrompido e o programa imprime o número de números únicos inseridos
