def cadrastro():
    try:
        arquivo = open('textoo')
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo não encontrado')
        arquivo = open('textoo', 'w')
        arquivo.close()
    else:
        nome = input('Digite o nome: ').capitalize()
        idade = int(input('digite a idade: '))
        arquivo = open('textoo', 'a')
        arquivo.write(f'{nome}\n')
        arquivo.write(f'{idade}\n')
        arquivo.close()


def lertexto():
    try:
        arquivo = open('textoo', 'r')
        dados = arquivo.readlines()
        arquivo.close()
    except FileNotFoundError:
        print('\033[31mNão há cadastros! insira cadastros.\033[m')
    else:
        dados2 = []
        for elemento in dados:
            dados2.append(elemento.rstrip('\n'))
        dados.clear()
        dados = dados2.copy()
        del dados2
        print('-'*26)
        print('Nome              idade')
        c = 0
        for valsor in range(0, len(dados)//2):
            print(f'\033[35m{dados[c]:<20}\033[36m{dados[c+1]}\033[m')
            c += 2


def escolha(string=''):
    while True:
        try:
            resp = int(input(string))
        except(ValueError, TypeError):
            menu()
            print('-' * 30)
            print('\033[35mDIGITE UMA OPÇÃO VÁLIDA\033[m')
            print('-' * 30)
        else:
            return resp


def menu():
    print('\033[31;7;1;3m------CADASTRO DE PESSOAS------\033[m')
    print('\033[32;1m1 - VER PESSOAS CADASTRADAS')
    print('2 - CADASTRAR PESSOAS')
    print('3 - SAIR\033[m')
