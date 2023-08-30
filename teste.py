"""
    assim se faz um comentário em linhas
"""
# e assim se faz um comentário em uma única linha

"""
type casting
numero = '10'

# para fazer o casting para inteiro basta colocá-lo na classe 'int'
numero2 = int(numero)

print(type(numero))
print(type(numero2))
"""

"""
print e input
"""

"""
try/except
    palavras reservadas no python
    servem para criar um código mais seguro e defensivo
    evitando quebra da aplicação
    
try:
except:
    raise ValueError("mensgem na tela")
    

# programa que solicita um numero ao usuario para mostrar o seu antecessor e seu sucessor
print('Antecessor e Sucessor!')
num = input("Digite um número: ") # retorna uma string

antecessor = 0
sucessor = 0

try:
    antecessor = int(num) - 1 #type casting
    sucessor = int(num) + 1 #type casting
except ValueError:
    print("Digite um número valido")
    raise ValueError# exibe onde está o erro


print(f"Número digitado: {num}")
print(f"O antecessor: {antecessor}")
print(f"Seu sucessor: {sucessor}")

print(type(num))
print(type(antecessor))
print(type(sucessor))


i = 0


while i <= 10:
    if i == 5:
        print("N quero mostrar este num")
        i += 1
        continue
    print(i)
    i += 1
    
print('Fora do escopo do while')

nomes = ["a", "b", "c", "d", "e"]
i = 0
for nome in nomes:
    print("Acessando pelo indice", nomes[i])
    #print(nome)
    i+=1
while i >= 10:
    if i == 15:
        print("Parei com o loop")
        i += 1
        break
    print(i)
    i += 1
"""


'''
lista
insert()
lista.append()
lista.copy()
lista.sort()
lista.sort(reverse=True)
lista.pop()
lista.remove()
'''

'''
fila

metodo gambiarra
from collections import deque
fila_como_deque.popleft()
'''

'''
pilha

'''

'''
    dicionario
dicionario = dict()
dicionario[123] = "456"
dicionario.update({"abc": "DEF"})

for chave, valor in dicionario:
    print(chave, valor)

'''