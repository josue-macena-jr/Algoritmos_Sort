"""Este algoritmo é um exemplo de bubble sorting para uma lista de N entradas numéricas"""

"""para gerar a lista, podemos fazer uma escolha randômica, ou inserir item a item conforme a escolha"""

from random import *

def initial():
        char = int(input("Escolha o modo de sorteio (1) para sorteio randômico, (2) para entrar item a item, ou (0) para encerrar:"))
        if char == 1:
            lst = randsort()
            print("Lista gerada!\n{}".format(lst))
            for i in range(len(lst)-1):
                lst = bubble(lst)
            print("Essa é a lista gerada aleatoriamente feito o bubble sorting...\n{}".format(lst))
        elif char == 2:
            lst = input("Insira os itens da lista a ser ordenda (use espaço para separar os números):\n").split()
            lst = [int(x) for x in lst] #linha necessária para converter uma lista de string em inteiros
            for i in range(len(lst)-1):
                lst = bubble(lst)
            print("Essa é a lista gerada aleatoriamente feito o bubble sorting...\n{}".format(lst))
        elif char == 0:
            print("Encerrando o programa!")
            pass
        else:
            print("Valor Inválido!\n")
            initial()

#gerando a lista randômica de tamanho fixo de 100

def randsort():
    lst = []
    for num in range(100):
        lst.append(randrange(0,101)) 
    return lst       

#Procedimento Bubble (a maior "bolha" é empurrada para o fim da lista)
#Aqui o maior valor é colocado como o primeiro, a medida que ele ele compara com o vizinho próximo e caso o vizinho seja maior, a variável "maior" é reescolhida, caso contrário é feito uma troca entre os dois valores
def bubble(lst):
    maior = lst[0]
    for k in range(len(lst)-1):
        if lst[k] < lst[k+1]:
            maior = lst[k+1]
        else:
            lst[k],lst[k+1] = lst[k+1],lst[k]
    return lst
        
initial()
