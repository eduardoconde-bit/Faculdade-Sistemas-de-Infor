from utilidadesCeV.caracteres import caracteres
teste = caracteres.asciiprint()


def leiadinheiro(valor='preço'):
    while True:
        notnumber = True
        p = input(valor).strip()
        for c in teste:  # verifica há caracteres não numéricos na entrada
            if c in p:
                notnumber = False

        if notnumber and p.count(',') == 0 and p != '':  # Válidar se é numero real simples com '.' ou não e sem ','
            if p.count('.') == 0 or (notnumber and p != '' and p.count('.') == 1):  # Vai testar se há apenas 1 ponto
                return float(p)  # Se houver mais de um ponto repete a entrada de dados

        elif notnumber and p != '' and p.count(',') == 1:  # Validar se é um número com vírgula
            p = p.replace(',', '.')
            return float(p)
        else:
            print('\033[31mERRO!, Digite um preço válido\033[m')


def leiaint(string):
    while True:
        print(string, end=' ')
        num = input()
        if num.isnumeric():
            return int(num)
        print('\033[31mERRO, Digite um número inteiro!\033[m')


def leiastring(string):
    while True:
        print(string, end=' ')
        nome = input().capitalize().strip()
        if nome.isalpha():
            return nome
        print('\033[31mERRO, digite valor correto!\033[m')
