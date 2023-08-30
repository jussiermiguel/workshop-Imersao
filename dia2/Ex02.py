'''
2. Crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h
mostre que ele foi multado e 7 reais por cada km
'''
# registro do radar
velocidade = input("Digite a velocidade que o carro passou no radar (em km): ")

try:
    velocidade_int = int(velocidade)# transformando o input pra o formato inteiro
except ValueError:
    raise ValueError("Valor inválido")

if velocidade_int > 80:
    print(f"{velocidade_int}km/h")
    print(f"Multa: R$ {(velocidade_int - 80)*7:.2f}")
    # velocidade que o carro passou - 80 (limite permitido) multiplicado por 7
    # 7 reais por cada km acima do limite
elif velocidade_int == 80:
    print(f"Limite atingido de {velocidade_int}km")
    print("Tenha mais cuidado. Sem multa")
else:
    print("Sem multa!")