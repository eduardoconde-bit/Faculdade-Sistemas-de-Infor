contas = [123456, 102030, 100200, 444444, 131002]#Número da conta dos usuários
valor = [3.900, 5.600, 8.900, 10.000, 15.000]#Valor correspondente a cada conta
nome = ['Luis', 'Lucas', 'Cassio', 'Marcelo', 'Caio']
transferencia = 0
def menu():
    print('\033[40m                                         \033[m')
    print('\033[30;1;46m            FIM DA OPERAÇÃO              \033[m')
print('\033[33;1m||||||||||||||| BANCO ABC |||||||||||||||\033[m')
print('\033[30;1;46m                BEM VINDO                \033[m')
print('\033[31;40;1m     Escolha a Opção correspondente      \033[m')
print('\033[31;1m1\033[m - \033[30mSaque\033[m | \033[31;1m2\033[m - \033[30mDepósito\033[m | \033[31;1m3\033[m - \033[30mTransferência\033[m')
resp = int(input('\033[31mEscolha sua opção: \033[m'))
resp_ = 'sim'
while resp_ in 'sim':
    if resp == 1:
        n = 0#contador
        nu_conta = int(input('\033[30mDigite o número da conta: \033[m'))#NUMERO DA CONTA
        if nu_conta in contas:#número da conta está na lista contas?
            while nu_conta != contas[n]:#faz a busca da conta
                n = n + 1
            print('\033[30mBEM  VINDO!\033[m \033[33m{}\033[m'.format(nome[n]))
            print('\033[31mVoçê tem \033[30m{:.3f} R$\033[m \033[31mem sua conta\033[m'.format(valor[n]))
            saque = float(input('Deseja retirar quanto: '))
            if saque <= valor[n]:
                print('\033[33;40;1mSaque liberado! Aguarde um instante\033[m')
                print('\033[30mVoçê sacou \033[31m{:.3f}\033[m \033[30mR$\033[m'.format(saque))
                print('\033[30mSaldo Atual \033[31m{:.3f}\033[m \033[30mR$\033[m'.format(valor[n] - saque))
            else:
                print('Saque Negado!')
                print('Limite de Retirada ultrapassado!')
        else:
            print('Não há conta correspondente ao que voçê Digitou!')
    elif resp == 2:
        n = 0
        nu_conta = int(input('Digite o número da conta: '))
        if nu_conta in contas:
            while nu_conta != contas[n]:
               n += 1
            valor2 = valor[n]
            print('\033[30mBEM  VINDO!\033[m \033[33m{}\033[m'.format(nome[n]))
            print('\033[30mVoçê tem {:.3f} R$ em sua conta\033[m'.format(valor[n]))
            deposito = float(input('\033[30mDeseja depositar quanto: \033[m'))
            if deposito <= 20.000 and deposito + valor[n] <= 20.000:
                print('\033[30mDepósito Liberado\033[m')
                print('\033[30mSaldo atual \033[31m{:.3f}\033[30m R$\033[m'.format(deposito + valor[n]))
            else:
                print('\033[31mDepósito negado devido ao limite de conta!\033[m')
        else:
            print('\033[31mNão há conta correspondente ao que voçê Digitou!\033[m')
    elif resp == 3:#Operação de transfêrencia
        n = 0#contador
        nu_conta = int(input('\033[30mDigite o número da conta: \033[m'))#NUMERO DA CONTA
        if nu_conta in contas:#número da conta está na lista contas?
            while nu_conta != contas[n]:#faz a busca da conta
                n += 1
            print('\033[30mBEM  VINDO!\033[m \033[33m{}\033[m'.format(nome[n]))
            print('\033[31mVoçê tem \033[30m{:.3f} R$\033[m \033[31mem sua conta\033[m'.format(valor[n]))
        transferencia = float(input('\033[34mDeseja transferir quanto:\033[m '))
        if transferencia <= valor[n]:
            resp3 = int(input('\033[34mDigite o número da conta para transferência:\033[m '))
            n = 0#contador
            if resp3 in contas:#número da conta está na lista contas?
                while resp3 != contas[n]:#faz a busca da conta
                    n = n + 1
            valor3 = valor[n]
            if (transferencia + valor3) <= 20.000:
                valor[n] = transferencia + valor3
                print('\033[33mTransferência efetuada!\033[m')
                print('\033[30mValor transferido! \033[31m{:.3f} R$\033[m'.format(transferencia))
            else:
                print('\033[30mtransferência negada devido ao limite da conta de envio!\033[m')
        else:
            print('\033[31m| NEGADO |valor de transferência excedido!\033[m')
    resp2 = input('\033[34mDeseja implementar usuários: ')
    if resp2 in 'sim':
        usuario = int(input('digite o numero da conta do novo usuário: '))
        nomeusuario = input('Digite o nome do usuário: ')
        valor3 = float(input('digite um valor para a conta: '))
        contas.append(usuario)
        valor.append(valor3)
        nome.append(nomeusuario)
    resp_ = input('Voçê deseja repetir o proccesso: \033[m')
menu()
