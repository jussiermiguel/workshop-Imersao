# programa que solicita um numero ao usuario para mostrar o seu antecessor e seu sucessor
print('Antecessor e Sucessor!')
num = int(input("Digite um número: ")) # solicitando o número

# calculando
antecessor = num - 1
sucessor = num + 1
# impressão dos resultados
print(f"Número digitado: {num}")
print(f"O antecessor: {antecessor}")
print(f"Seu sucessor: {sucessor}")