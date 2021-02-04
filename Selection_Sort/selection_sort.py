"""Este algoritmo é um exemplo de selection sorting para uma lista de N entradas numéricas"""

"""para gerar a lista, podemos fazer uma escolha randômica, ou inserir item a item conforme a escolha"""

from random import *

#gerando a lista randômica de tamanho fixo de 100

def initial():
        char = int(input("Escolha o modo de sorteio (1) para sorteio randômico, (2) para entrar item a item, ou (0) para encerrar:"))
        if char == 1:
            lst = [randrange(0,6) for num in range(5)]
            print("Lista gerada!\n{}".format(lst))
            lst = selection(lst)
            print("Essa é a lista ordenada feito o selection sorting...\n{}".format(lst))
        elif char == 2:
            lst = input("Insira os itens da lista a ser ordenda (use espaço para separar os números):\n").split()
            lst = [int(x) for x in lst] #linha necessária para converter uma lista de string em inteiros
            lst = selection(lst)
            print("Essa é a lista ordenada feito o selection sorting...\n{}".format(lst))
        elif char == 0:
            print("Encerrando o programa!")
            pass
        else:
            print("Valor Inválido!\n")
            initial()

#Procedimento Selection (o item é comparado com seus predecessores na lista)
#Aqui o pivô é o primeiro elemento, e é encontrado o menor valor da lista de predecessores. Dado esse menor valor, ambos trocam de lugar, e o próximo pivô é escolhido, seguindo até a ordenação completa. Caso não haja um menor valor que o pivô, nada é alterado.

def selection(lst):
    k = 0
    while k < len(lst):
        pivo = menor = lst[k]
        for t in lst[lst.index(pivo)+1:]:
            if t < menor:
                menor = t
                #print(t)
        lst[lst.index(menor)],lst[lst.index(pivo)] = lst[lst.index(pivo)],lst[lst.index(menor)]
        k += 1
    return lst

initial()