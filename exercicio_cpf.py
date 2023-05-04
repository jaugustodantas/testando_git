digitos_cpf= input('Digite somente os numeros do cpf: ')
#lista_teste = list(digitos_cpf)
numero_calculado1 = 0
numero_calculado2 = 0 
multiplicador = 10
multiplicador2 = 11
for n in digitos_cpf:
    if multiplicador >= 2:
        numero_calculado1 += int(n) * multiplicador
        multiplicador-=1
    else:
        break
for n in digitos_cpf:
    if multiplicador2 >= 2:
        numero_calculado2 += int(n) * multiplicador2
        multiplicador2-=1
    else:
        break


numero_calculado1 = numero_calculado1*10
numero_calculado1 = numero_calculado1 %11
primeiro_digito = 0 if numero_calculado1 > 9 else numero_calculado1
print(f'O primeiro digito do cpf é {primeiro_digito}')
numero_calculado2 = numero_calculado2*10
numero_calculado2 = numero_calculado2 %11
segundo_digito = 0 if numero_calculado2 > 9 else numero_calculado2
print(f'O primeiro digito do cpf é {segundo_digito}')