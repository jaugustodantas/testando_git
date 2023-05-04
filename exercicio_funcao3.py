# def duplicar (x):
#     return x * 2

# def triplica (x):
#     return x*3

# def quadriplica (x):
#     return x * 4


# x = 2
# x2= duplicar(x)
# x3= triplica(x)
# x4 = quadriplica(x)

# print(f' O dobro de {x} é {x2}, o triplo é {x3} e o quadruplo é {x4}')

def criando_multiplicador (multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    
    return multiplicar


x2 = criando_multiplicador(2)
x3 = criando_multiplicador(3)
x4 = criando_multiplicador(4)

print(x2(2))
print(x3(2))
print(x4(2))