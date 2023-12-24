#Aluno: Luis Eduardo Furtado Conde 202111140024

class Node():
    '''
    Classe represantando um nó
    '''
    def __init__(self, data):
        self.node = data
        self.next = None

#Estrutura de Dados Fila
class Queue():
    '''
    Classe Representando uma Estruturas de Dados Fila
    '''
    def __init__(self):
        self.size = 0
        self.firstNode = None
        self.lastNode = self.firstNode
    
    def toQueue(self, elemento):
        '''
        Enfileirar um elemento
        '''
        node = Node(elemento)

        if self.lastNode == None:
            self.lastNode = node

        else:
            self.lastNode.next = node
            self.lastNode = node
            
        if self.firstNode == None:
            self.firstNode = node

        self.size += 1

    def dequeue(self):
        '''
        Desenfileirar um elemento
        '''
        if self.firstNode != None:
            node = self.firstNode.node
            self.firstNode = self.firstNode.next

            self.size -= 1

            return node
        else:
            pass        

    def lenQueue(self):
        '''
        Retorna o tamanho da fila
        '''
        return self.size
