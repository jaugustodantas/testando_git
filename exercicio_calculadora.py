while True:
    erro_letras = False
    numero_1_convertido = None
    numero_2_convertido = None
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite um número: ")
    operador = input("Digite o operador *,/,+,-: ")
    teste_numero_1 = numero_1.isdigit()
    teste_numero_2 = numero_2.isdigit()
    if teste_numero_1:
        numero_1_convertido = int(numero_1)
    elif teste_numero_1 == False:
        try:
            numero_1_convertido = float(numero_1)
        except:
            erro_letras = True
            print("O valor de entrada não é um número")

    if teste_numero_2:
        numero_2_convertido = int(numero_2)
    elif teste_numero_2 == False:
        try:
            numero_2_convertido = float(numero_2)
        except:
            erro_letras = True
            print("O valor de entrada não é um número")

    tamanho_operador = len(operador) > 0 and len(operador) <=1
    if tamanho_operador and erro_letras is False:
        if operador == "+":
            soma = numero_1_convertido + numero_2_convertido
            print(f"A soma de {numero_1}{operador}{numero_2} é: {soma}")
        elif operador == "-":
            subtracao = numero_1_convertido - numero_2_convertido
            print(f"A subtracao de {numero_1}{operador}{numero_2} é: {subtracao}")
        elif operador == "*":
            multiplicacao = numero_1_convertido * numero_2_convertido
            print(f"A multiplicacao de {numero_1}{operador}{numero_2} é: {multiplicacao}")
        elif operador == "/":
            try:
                divisao = numero_1_convertido / numero_2_convertido
                print(f"A multiplicacao de {numero_1}{operador}{numero_2} é: {divisao}")
            except:
                print("Não é possível dividir por 0")
    elif not tamanho_operador:
        print("Só é permitido um operador")

    continuar = input ("Para sair digite [s]")
    teste_gatilho = continuar.lower().startswith('s')
    if teste_gatilho:
        break

