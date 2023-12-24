import os
print('Se você estiver na HOME. Para ver o código clique em showfiles no canto superior esquerdo!')
print('-'*50)
print('LUIS EDUARDO FURTADO CONDE 202111140024')
while True:
    print('Escolha as questões!')
    print('(1) - Questão 1 | (2) - Questão 2')
    resp = int(input('Qual questão executar?: '))
    if resp == 1:
        print('-'*50)
        print('Questão 1')
        os.system('python3 questao1.py')
    elif resp == 2:
        print('-'*50)
        print('Questão 2')
        os.system('python3 questao2.py')
    else:
        print('Opção inexistente!!')
    resp = input('Continuar (ENTER) | Finalizar (s): ').lower().strip()
    if resp == 's':
        break
    os.system('clear')