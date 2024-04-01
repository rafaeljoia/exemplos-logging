from utils_log import log_decorator

"""
Criado uma função chamada log_decorator, onde é considerada uma wrapper, é uma função que recebe outra função.
Para utilizar o registro de log, basta incluir o decorator em cima da função.

"""

@log_decorator
def soma(x, y):
    return x + y

print(soma(2 ,"3"))