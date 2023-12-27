espressao = input('Digite a espressão: ')
pilha = []
for simb in espressao:
    if simb == '(':#parentese aberto
        pilha.append('(')
    elif simb == ')':#parentese fechado
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
