

from functools import reduce

lista = [2, 4, 3, 7, 5, 8, 10]
salida1 = list(filter(lambda x: (x % 2 != 0), lista))
print("Números impares usando la expresión lambda: ", salida1 )

def sum(a, b):
    return a + b

total = reduce(sum, salida1)
print(total)
