hora_entrada = input("Digite uma hora entre 0 e 23 horas: ")
hora_convertida_inteiro = int(hora_entrada)
intervalo_manha = hora_convertida_inteiro >= 0 and hora_convertida_inteiro <= 11
intervalo_tarde = hora_convertida_inteiro >= 12 and hora_convertida_inteiro <= 17
intervalo_noite = hora_convertida_inteiro >= 18 and hora_convertida_inteiro <= 23

if intervalo_manha:
    print("Bom dia")
elif intervalo_tarde:
    print("Boa tarde")
elif intervalo_noite:
    print("Boa noite")
else:
    print("hora invalida")