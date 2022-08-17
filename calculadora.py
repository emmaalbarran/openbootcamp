# ----- calculadora.py ---------
import operaciones as o
import pprint

def main():
    suma = o.suma(2, 2)
    resta = o.resta(5,3)
    multiplicacion = o.multiplicar(2,5)
    division = o.dividir(10,2)
    print("Suma es igual a: ", suma)
    print("Resta es igual a: ", resta)
    print("Multiplicacion es igual a: ", multiplicacion)
    print("Division es igual a: ", division)

if __name__ == '__main__':
    main()
    
 # ----- operaciones.py ---------
 def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

def multiplicar (a,b):
    return a * b

def dividir (a,b):
    return a / b
