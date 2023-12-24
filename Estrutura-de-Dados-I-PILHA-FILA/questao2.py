#Aluno: Luis Eduardo Furtado Conde 202111140024

from random import randint
from Queue import Queue #Consultar Módulo Queue
from Stack import Stack #Consultar Módulo Stack

#Instanciando Objetos
queuePar = Queue()
queueImpar = Queue()
pilha = Stack()

print('-'*50)
while True: #Valores gerados Aleatoriamente, -20 a 50 (inteiros)
    number = randint(-20, 50)
    if number == 0:
        print('"0" finalizou a entrada de dados do programa')
        break
    else:
        if number % 2 == 0:
            queuePar.toQueue(number)
        else:
            queueImpar.toQueue(number)

limit = queuePar.size if queuePar.size > queueImpar.size else queueImpar.size
sizeQueueImpar  = queueImpar.size
sizeQueuePar  = queuePar.size

#Valores alternados 1 ìmpar e um 1 par sucessivamente
for i in range(1, limit+1):
    #Trata os valores ímpares
    if sizeQueueImpar <= limit and sizeQueueImpar > 0:
        valueImpar = queueImpar.dequeue()
        if valueImpar != None:
            #Adiciona o valor se ele for positivo
            if valueImpar > 0:
                pilha.stackup(valueImpar)
            #Retira elementos da pilha se o valor da fila ÍMPAR for negativo
            else:
                if not pilha.isStackEmpty():
                    pilha.unstack()

    #Trata os valores pares
    if sizeQueuePar <= limit and sizeQueuePar > 0:
        valuePar = queuePar.dequeue()
        if valuePar != None:
            #Adiciona o valor se ele for positivo
            if valuePar >= 0:
                pilha.stackup(valuePar)
            #Retira elementos da pilha se o valor da fila PAR for negativo
            else:
                if not pilha.isStackEmpty():
                    pilha.unstack()
    
print('Contéudo da Pilha: ', end='')
pilha.show()
print('-'*50)