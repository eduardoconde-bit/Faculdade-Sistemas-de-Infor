frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra (A) aparece {} vezes'.format(frase.count('A')))
print('A letra A apareceu primeiramente na posição {}'.format(frase.find('A') + 1))
print('A letra A apareceu pela ultima vez na posição {}'.format(frase.rfind('A')-1))


