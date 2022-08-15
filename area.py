def area (a, b, r):

    def t(a, b):
        at = (a * b) / 2
        print('El area del triangulo es: ', at )

    def c(r):
        import math
        ac = 2 * r * math.pi
        print('El area del triangulo es: ', ac)

    t(a, b)
    c(r)

area (10, 5, 8)
