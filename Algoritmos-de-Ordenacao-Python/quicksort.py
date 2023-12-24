#LUIS EDUARDO FURTADO CONDE 202111140024

#Quicksort
def quickSort(alist): #Uma lista para ordenação
    #counter_comparation = 0 # Contador de Comparações
    #counter_swap = 0 # Contador de Trocas
    quickSortHelper(alist,0,len(alist)-1)

#uso de recursão
def quickSortHelper(alist,first,last):
    if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)
    #print('terminou')

#Implementa (Conquistar para Dividir)
def partition(alist,first,last):
   pivotvalue = alist[first] #Alvo ou Pivot

   leftmark = first+1 # Marcador de Posição leftmark
   rightmark = last # Marcador de Posição Rightmark

   done = False
   while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp 
       
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

counter_comparation = 0 # Contador de Comparações
counter_swap = 0 # Contador de Trocas