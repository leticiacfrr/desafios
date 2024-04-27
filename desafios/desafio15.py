#import serve pra importar informações de um biblioteca
#from+(nome da biblioteca)+import server para importar algo especifico
# na biblioteca math existe as funções de arredondamento (ceil+, floor-), trunc(eliminar os números depois da virgula), pow(potencia), sqr(raiz) e factorial(fatoração)
import math
n = int(input('digite um número: '))
raiz = math.sqrt(n)
print('a raiz é {}'.format(math.floor(raiz)))