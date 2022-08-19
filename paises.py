def s():
    ingresar = input("Ingresa paises separados por coma: ")
    paises = ingresar.split(',')
    paises.sort()
    paises2 = set(paises)
    print(paises2)

s()
