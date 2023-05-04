lista_de_compras = []
variavel_de_apoio = ''
vi = 0
while True:
    valor_de_acao = input('digite I para inserir,A para apagar e M para mostrar os itens da lista e S para sair ').lower()
    if valor_de_acao == 'i':
        entrada_da_lista= input('Digite os itens da sua lista de compras os separando por vígula , :').lower()
        tupla_de_apoio = tuple(entrada_da_lista)
        for i,v in enumerate(tupla_de_apoio):
            if v != ',' and v !=' ':
                variavel_de_apoio += v
            elif v == ',' or v ==' ':
                lista_de_compras.append(variavel_de_apoio)
                variavel_de_apoio = ''   
        lista_de_compras.append(variavel_de_apoio)
        variavel_de_apoio = ''
    elif valor_de_acao == 'a':
        qual_item_excluir = input('Digite o ítem que deseja excluir: ').lower()
        try:
            vi=lista_de_compras.index(qual_item_excluir)
            lista_de_compras.pop(vi)
        except:
            print(f'O item {qual_item_excluir} não está na lista')
    elif valor_de_acao == 'm':
        print(lista_de_compras)
    elif valor_de_acao == 's':
        break



print(lista_de_compras)