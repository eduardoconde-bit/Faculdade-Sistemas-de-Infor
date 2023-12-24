#Luis Eduardo Furtado Conde 202111140024

#countsort
def countingSort(inputArray):
    counter_comparation = 0 # Contador de Comparações
    
    maxElement= max(inputArray)

    countArrayLength = maxElement+1
    
    countArray = [0] * countArrayLength
    
    for el in inputArray: 
        countArray[el] += 1

    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1
    counter_comparation = len(outputArray)
    return [outputArray, counter_comparation]