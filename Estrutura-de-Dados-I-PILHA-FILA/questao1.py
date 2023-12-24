#Aluno: Luis Eduardo Furtado Conde 202111140024

from Stack import Stack

stack = Stack()

#MENU
print('-'*50)
number = int(input('Digite um valor para conversão: '))
print('(1) - BINÁRIO |  (2) - OCTAL |  (3) - HEXADECIMAL')
print('-'*50)

base = int(input('PARA QUAL BASE CONVERTER?: '))

DECIMAL = number #valor na base 10 para a exibição

#Desempilha e exibe o valor convertido ao usuário
def show(pile):
    for i in range(1, pile.sizeStack() + 1):
        value = pile.unstack()
        print(value, end='')
    print()
    print('-'*50)

#Decimal para Binário
if base == 1:
    flag = number < 0
    number = abs(number)
    result  = number
    if number > 1:
            while result != 0:
                result = result // 2
                stack.stackup(number % 2)
                number = result
            if flag:
                stack.stackup('-')
            #Exibição
            print('-'*50)
            print(f'Decimal: {DECIMAL} | Binário: ', end = '')
            show(stack)
    else:
        if number == 0:
            print('0 (b2)')
        if number == 1:
            print('1 (b2)')


# (Lembrar) Ainda é mais prático definir isso em uma única função e definir a conversões por parâmetros

#Decimal para octal
if base == 2:
    flag = number < 0
    number = abs(number)
    result  = number
    if number > 0:
            while result != 0:
                result = result // 8
                stack.stackup(number % 8)
                number = result
            if flag:
                stack.stackup('-')
            
            #Exibição
            print('-'*50)
            print(f'Decimal: {DECIMAL} | Octal: ', end = '')
            show(stack)


#Decimal para Binário
if base == 3:
    HEXA = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'} #Relaciona os valores de 10 a 15 com suas respectivas representações em hexadecimal (de A a F)
    flag = number < 0 #Usada para definir números valores negativos
    number = abs(number)
    result  = number
    if number > 0:
            while result != 0:
                result = result // 16
                if number % 16 > 9:
                    stack.stackup(HEXA[number % 16])
                else:
                    stack.stackup(number % 16)
                number = result
            if flag:
                stack.stackup('-')
            #Exibição
            print('-'*50)
            print(f'Decimal: {DECIMAL} | Hexadecimal: ', end = '')
            show(stack)