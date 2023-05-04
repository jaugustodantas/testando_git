"""
    Está é a solução 2 do problema da aula 124 do curso do prof Luiz Otávio da udemy. 
    Solução usando funções dentro de funções ( o que eu acho meio estranho)
"""
import random
perguntas = [
    {
        'Pergunta' :    'Quanto é 2 + 2 ?',
        'Opcoes' : ['1','3','4','5'],
        'Resposta': '4'

    },
    {
        'Pergunta' :    'Quanto é 5*5 ?',
        'Opcoes' : ['25','55','10','51'],
        'Resposta': '25'
    },
    {
        'Pergunta' :    'Quanto é 10 / 2 ?',
        'Opcoes' : ['1','0','4','5'],
        'Resposta': '5'
    }
]
def teste (x):
      print(perguntas[x].get('Pergunta'))  #o número radom está chamando a pergunta
      def pega_opcoes (x):
            print('Alternativas: ')
            options = perguntas[x].get('Opcoes')
            for o in options: 
                print(o)
            def checar_resposta (x):
             while True:
                 resposta = input("Qual a sua resposta ? ")
                 if resposta == perguntas[x].get('Resposta'):
                    print('Acertô miseravi')
                    break
                 else:
                    resetar = input('Resposta incorreta, para tentatar novamente digite s: ').lower()
                 if resetar != 's':
                     break
            return checar_resposta
      return pega_opcoes


numero_aleatorio= random.randrange(0,3)
variavel_de_apoio = teste(numero_aleatorio)
var1 = variavel_de_apoio(numero_aleatorio)
var2 = var1(numero_aleatorio)
var2