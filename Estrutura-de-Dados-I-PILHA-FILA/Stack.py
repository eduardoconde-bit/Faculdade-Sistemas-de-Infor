#Aluno: Luis Eduardo Furtado Conde 202111140024

class Stack():
    def __init__(self):
        self.size = 0
        self.elements = []
    
    def stackup(self, element):
        #Empilha elementos
        self.elements += [element]
        self.size += 1
    
    def show(self):
        '''
        Exibe a pilha inteira
        '''
        if not self.isStackEmpty():
            position = 0
            while position < self.size:
                print(self.elements[position], end= ' ')
                position += 1 
            print()
        else:
            print('Pilha Vazia!')
    
    def isStackEmpty(self):
        return self.elements == []
    
    def unstack(self):
        '''
        Função Desempilha
        '''
        if self.isStackEmpty():
            print("Pilha Vazia! operação abortada!")
        else:
            pos = len(self.elements) - 1
            topStack = self.elements[pos]
            self.elements = self.elements[:-1]
            self.size -= 1
            return topStack

    def sizeStack(self):
        return self.size