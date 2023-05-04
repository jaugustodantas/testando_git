numero_convertido = None
entrada_numero_1 = input("digite um numero inteiro: ")

if "." in entrada_numero_1:
    print("o numero deve ser um inteiro")
elif "." not in entrada_numero_1:
   # print("até aqui funcionou")
    numero_convertido = int(entrada_numero_1)
    #print(type(numero_convertido))
    if numero_convertido%2 ==0:
        print(f"O numero {numero_convertido} é par")
    elif numero_convertido%3 ==0:
        print(f"O número {numero_convertido} é impar")