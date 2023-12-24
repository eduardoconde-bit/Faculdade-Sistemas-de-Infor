#LUIS EDUARDO FURTADO CONDE 202111140024

#Bubble Sort Implementado Complexidade O(n^2)

def bubbleSort(alist):
    counter_comparation = 0 # Contador de Comparações
    counter_swap = 0 # Contador de Trocas
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            #Realiza as comparações e efetua as trocas
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                counter_swap += 1
            counter_comparation += 1
    return [counter_comparation, counter_swap] #Retorna uma lista com contagens de de comparação e e trocas