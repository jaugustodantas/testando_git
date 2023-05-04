def multiplicador (*arg):
    total_multiplicacao =1
    for n in arg:
        total_multiplicacao *= n
    return total_multiplicacao


resultado= multiplicador(5,2,10,2)
print(resultado)