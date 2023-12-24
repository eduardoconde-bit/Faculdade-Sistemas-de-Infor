#LUIS EDUARDO FURTADO CONDE 202111140024

from random import randint #Módulo para aleatorizar números
from os import system #limpar tela do terminal
import timeit #Facilita a medição de tempo de execução das funções

#MÓDULOS CRIADOS COM AS IMPLEMETAÇÕẼS DE CADA ALGORITMO DE ORDENAÇÃO
from bubble import bubbleSort
from quicksort import quickSort
from countingsort import countingSort

system('clear')

lista = [] #Definição da Lista

print('Algoritmos de Ordenação')
print('(1) - BubbleSort \n(2) - QuickSort\n(3) - CountingSort')
resp = int(input('Digite sua opção: '))
if resp == 1:
    system('clear')
    print('Quantidade de Valores a serem Ordenados com BubbleSort')
    print(' (1) - 10 valores | (2) - 100 valores | (3) - 1000 valores | (4) - 10000 valores')
    resp = int(input('Digite sua opção: '))
    
    print('-'*50)
    if resp == 1:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 11):
                lista.append(randint(-50, 50)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 11):
                lista.append(i) #Valores negativos e positivos
        print('Ordenando Com BubbleSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        counters = bubbleSort(lista)
        fim = timeit.default_timer()
        print('LISTA ORDENADA \n')
        print(lista)
        print(f'\nForam realizadas {counters[0]} comparações\nE realizadas {counters[1]} trocas')
        print('-'*50)
        print (f'Tempo de Execução do Bubble Sort: {fim - inicio} seconds (Impossível Medir. Tempo Ridiculamente Pequeno)')
    if resp == 2:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 101):
                lista.append(randint(-50, 50)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 101):
                lista.append(i) #Valores negativos e positivos
        
        print('Ordenando Com BubbleSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        counters = bubbleSort(lista)
        fim = timeit.default_timer()
        print('LISTA ORDENADA \n')
        print(lista)
        print(f'\nForam realizadas {counters[0]} comparações\nE realizadas {counters[1]} trocas')
        print('-'*50)
        print (f'Tempo de Execução do Bubble Sort: {fim - inicio} seconds')
    if resp == 3:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 1001):
                lista.append(randint(-1000, 1000)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 1001):
                lista.append(i) #Valores negativos e positivos
        
        print('Ordenando Com BubbleSort VETOR DE 1000 ELEMENTOS...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        counters = bubbleSort(lista)
        fim = timeit.default_timer()
        print('LISTA ORDENADA \n')
        print(lista)
        print(f'\nForam realizadas {counters[0]} comparações\nE realizadas {counters[1]} trocas')
        print('-'*50)
        print (f'Tempo de Execução do Bubble Sort: {fim - inicio} seconds')
    if resp == 4:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 10001):
                lista.append(randint(-10001, 10001)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 10001):
                lista.append(i) #Valores negativos e positivos
        
        print('Ordenando Com BubbleSort VETOR DE 10000 ELEMENTOS...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista[0:2501], '... Encurtado') #mostra uma parte apenas da lista para não ficar enorme a exibição no terminal
        print('-'*50)
        print('\n\nORDENANDO OS VALORES....')
        inicio = timeit.default_timer()
        counters = bubbleSort(lista)
        fim = timeit.default_timer()
        print('LISTA ORDENADA \n')
        print(lista)
        print(f'\nForam realizadas {counters[0]} comparações\nE realizadas {counters[1]} trocas')
        print('-'*50)
        print (f'Tempo de Execução do Bubble Sort: {fim - inicio} seconds')
        
#QUICKSORT
elif resp == 2:
    system('clear')
    print('Quantidade de Valores a serem Ordenados com QuickSort')
    print(' (1) - 10 valores | (2) - 100 valores | (3) - 1000 valores | (4) - 10000 valores')
    resp = int(input('Digite sua opção: '))
    print('-'*50)
    if resp == 1:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 11):
                lista.append(randint(-50, 50)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 11):
                lista.append(i) #Valores negativos e positivos
            
        print('\nOrdenando Com QuickSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        quickSort(lista)
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        print(lista)
        print('-'*50)
        print (f'Tempo de Execução do QuickSort: {fim - inicio} seconds (Impossível Medir. Tempo Ridiculamente Pequeno)')
    if resp == 2:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 101):
                lista.append(randint(-50, 50)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 101):
                lista.append(i) #Valores negativos e positivos
            
        print('\n Com QuickSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        quickSort(lista)
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        print(lista)
        print('-'*50)
        print (f'Tempo de Execução do QuickSort: {fim - inicio} seconds')
    if resp == 3:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 1001):
                lista.append(randint(-1000, 1000)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 1001):
                lista.append(i) #Valores negativos e positivos
            
        print('\nOrdenando Com QuickSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        quickSort(lista)
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        print(lista)
        print('-'*50)
        print (f'Tempo de Execução do QuickSort: {fim - inicio} seconds')
    if resp == 4:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 10001):
                lista.append(randint(-10000, 10000)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 10001):
                lista.append(i) #Valores negativos e positivos
            
        print('\nOrdenando Com QuickSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista[0:2500], '... Encurtado')
        print('-'*50)
        inicio = timeit.default_timer()
        quickSort(lista)
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        print(lista)
        print('-'*50)
        print (f'Tempo de Execução do QuickSort: {fim - inicio} seconds')

#COUNTING SORT
elif resp == 3:
    system('clear')
    print('Quantidade de Valores a serem Ordenados com CountingSort')
    print(' (1) - 10 valores | (2) - 100 valores | (3) - 1000 valores | (4) - 10000 valores')
    resp = int(input('Digite sua opção: '))
    print('-'*50)
    if resp == 1:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 11):
                lista.append(randint(1, 100)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 11):
                lista.append(i) #Valores negativos e positivos
            
        print('\nOrdenando Com CountingSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        counters = countingSort(lista)
        print(counters[0])
        print(f'\nForam realizadas {counters[1]} "comparações"\nEsse Algoritmo não suporta trocas pois é baseado em Mapeamento')
        print('-'*50)
        print (f'Tempo de Execução do CountingSort: {fim - inicio} seconds (Impossível Medir. Tempo Ridiculamente Pequeno)')
    if resp == 2:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 101):
                lista.append(randint(1, 100)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 101):
                lista.append(i) #Valores negativos e positivos
            
        print('\nOrdenando Com CountingSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        counters = countingSort(lista)
        print(counters[0])
        print(f'\nForam realizadas {counters[1]} "comparações"\nEsse Algoritmo não suporta trocas pois é baseado em Mapeamento')
        print('-'*50)
        print (f'Tempo de Execução do CountingSort: {fim - inicio} seconds')
    if resp == 3:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 1001):
                lista.append(randint(1, 1000)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 1001):
                lista.append(i) #Valores negativos e positivos
            
        print('\nOrdenando Com CountingSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista)
        print('-'*50)
        inicio = timeit.default_timer()
        counters = countingSort(lista)
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        counters = countingSort(lista)
        print(counters[0])
        print(f'\nForam realizadas {counters[1]} "comparações"\nEsse Algoritmo não suporta trocas pois é baseado em Mapeamento')
        print('-'*50)
        print (f'Tempo de Execução do CountingSort: {fim - inicio} seconds')
    if resp == 4:
        print('ORDEM DOS VALORES\n(1) - aleátórios\n(2) - Ordenados Descendentes')
        option = int(input('resposta:'))
        if option == 1: 
            for i in range(1, 10001):
                lista.append(randint(1, 10000)) #Valores negativos e positivos
        elif option == 2:
            for i in range(1, 10001):
                lista.append(i) #Valores negativos e positivos
            
        print('\nOrdenando Com QuickSort...\n')
        print('LISTA ANTES DA ORDENAÇÃO \n')
        print(lista[0:2500], '... Encurtado')
        print('-'*50)
        inicio = timeit.default_timer()
        counters = countingSort(lista)
        fim = timeit.default_timer()
        print('\nLISTA ORDENADA \n')
        counters = countingSort(lista)
        print(counters[0])
        print(f'\nForam realizadas {counters[1]} "comparações"\nEsse Algoritmo não suporta trocas pois é baseado em Mapeamento')
        print('-'*50)
        print (f'Tempo de Execução do CountingSort: {fim - inicio} seconds')