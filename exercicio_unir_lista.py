lista_cidade = ['Salvador','Ubatuba','Belo Horizonte']
lista_estado = ['BA','SP','MG','RJ']

def medidor_de_lista(lista1,lista2):
     novalista =[]
     teste =()
     if len(lista2) > len(lista1):
        for x in range(len(lista1)):
            teste = (lista1[x],lista2[x])
            novalista.append(teste)
        return novalista
     elif len(lista1) > len(lista2):
        for x in range(len(lista2)):
            teste = (lista2[x],lista1[x])
            novalista.append(teste)
        return novalista
     else:
        for x in range(len(lista2)):
            teste = (lista2[x],lista1[x])
            novalista.append(teste)
        return novalista
    
    


    
a=medidor_de_lista(lista_cidade,lista_estado)
print(a)


# print(tamanho_lista1,type(tamanho_lista1))
# print(tamanho_lista2,type(tamanho_lista2))