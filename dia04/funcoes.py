'''

'''
def soma(x: int | float, y: int| float) -> int | float:
    """Soma x + y e retorna o resultado"""#documentando
    # resultado = x + y
    return x + y

def print_subtracao(x: int| float, y: int | float) -> None: # none retorna nada
    print(f"resultado = {x - y}")    
    #return None

def soma_sem_parametro() -> int | float:
    x = 5
    y = 5
    return x + y
    #print()