"""Este algoritmo é um exemplo de insertion sorting para uma lista de N entradas numéricas"""

"""para gerar a lista, podemos fazer uma escolha randômica, ou inserir item a item conforme a escolha"""

from random import randrange

def initial():
        char = int(input("Escolha o modo de sorteio (1) para sorteio randômico, (2) para entrar item a item, ou (0) para encerrar:"))
        if char == 1:
            lst = [randrange(0,101) for num in range(100)]
            print("Lista gerada!\n{}".format(lst))
            for i in range(len(lst)-1):
                lst = insertion_sort(lst)
            print("Essa é a lista ordenada feito o insertion sorting...\n{}".format(lst))
        elif char == 2:
            lst = input("Insira os itens da lista a ser ordenda (use espaço para separar os números):\n").split()
            lst = [int(x) for x in lst] #linha necessária para converter uma lista de string em inteiros
            for i in range(len(lst)-1):
                lst = insertion_sort(lst)
            print("Essa é a lista ordenada feito o insertion sorting...\n{}".format(lst))
        elif char == 0:
            print("Encerrando o programa!")
            pass
        else:
            print("Valor Inválido!\n")
            initial()

def insertion_sort(lst):
    ordered_lst = []
    for k in range(len(lst)):
        if lst[k]>lst[k+1]:
            ordered_lst.append(lst.pop(k+1))
            ordered_lst += lst
    return ordered_lst


initial()