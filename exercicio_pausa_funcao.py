def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    args.__add__:1
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)