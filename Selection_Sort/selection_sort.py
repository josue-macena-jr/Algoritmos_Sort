"""Este algoritmo é um exemplo de selection sorting para uma lista de N entradas numéricas"""

"""para gerar a lista, podemos fazer uma escolha randômica, ou inserir item a item conforme a escolha"""

from random import *

#gerando a lista randômica de tamanho fixo de 100

def initial():
        char = int(input("Escolha o modo de sorteio (1) para sorteio randômico, (2) para entrar item a item, ou (0) para encerrar:"))
        if char == 1:
            lst = [randrange(0,101) for num in range(101)]
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
#Aqui o pivô é o primeiro elemento, e é encontrado o menor valor da lista de predecessores. Dado esse menor valor, ambos trocam de lugar, esse elemento então é separado numa lista ordenada e retirado da lista original e o próximo pivô é escolhido como sendo o primeiro novo elemento da lista, seguindo até a ordenação completa. Caso não haja um menor valor que o pivô, nada é alterado.

def selection(lst):
    ordered_lst = []
    while len(lst) != 0:
        menor = lst[0]
        for t in lst[1:]:
            if t < menor:
                menor = t
        lst[lst.index(menor)],lst[0] = lst[0],lst[lst.index(menor)]
        ordered_lst.append(lst.pop(0))
    return ordered_lst

initial()