def verificador (x):
    try:
        if x % 2 == 0:
            return ('par')
        
        return('impar')
    except:
        return ('somente numero > 0')
    

teste = verificador("a")

print(teste)