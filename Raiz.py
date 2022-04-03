from cmath import sqrt


a = int(input('Digite o Valor de A:'))
b = int(input('Digite o Valor de B: '))
c = int(input('Digite o Valor de C: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('Delta Negativo')
else:
    raiz_quadrada = sqrt(delta)
    x1 = (-b + raiz_quadrada) / 2*a
    x2 = (-b - raiz_quadrada) / 2*a

    print("A Raiz Quadrada", x1, "e", x2)
