#Escreva um programa que solicite ao usuário que insira números até que ele insira um número negativo. Em seguida, imprima o maior número inserido.

maior_numero = float('-inf')  # Inicializa a variável maior_numero com o menor valor possível para números de ponto flutuante
numero = float(input("Por favor, insira um número (ou um número negativo para sair): "))  # Solicita ao usuário que insira um número e o converte para ponto flutuante, armazenando-o na variável numero

while numero >= 0:  # Inicia um loop while que continuará enquanto o número inserido for maior ou igual a zero
    if numero > maior_numero:  # Verifica se o número inserido é maior que o maior número encontrado até agora
        maior_numero = numero  # Se for, atualiza o valor do maior número
    numero = float(input("Por favor, insira um número (ou um número negativo para sair): "))  # Solicita ao usuário que insira outro número e o converte para ponto flutuante, atualizando a variável numero

if maior_numero != float('-inf'):  # Verifica se algum número válido foi inserido (ou seja, se o valor do maior número foi atualizado durante o loop)
    print("O maior número inserido é:", maior_numero)  # Se sim, imprime o maior número encontrado
else:
    print("Nenhum número válido foi inserido.")  # Se não, imprime uma mensagem informando que nenhum número válido foi inserido
