'''
1 crie um programa que receba uma idade e retorne se pode obter a carteira de mostorista (cnh)
'''
# adicione um input
idade = input("Digite a sua idade: ")
# verifique se tem a idade correta
try:
    idade_int = int(idade)
    if idade_int >= 18:
        print(f"Com {idade_int} anos você está apto. Pode tirar a CNH! ")# retorne se tem
    else:
        print(f"Com {idade_int} anos, você ainda não pode tirar a CNH!")
except ValueError:
    print("Digite um valor válido")
    raise  