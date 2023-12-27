while True:
    try:
        print('----Divisor de dois números---')
        n = int(input('digite número: '))
        n2 = int(input('digite um número: '))
        v = n/n2
    except ZeroDivisionError:
        print('Erro de divisão por zero')
        print('Tente não dividir números por zero')
    except TypeError:
        print('Erro de tipo')
    except ValueError:
        print('Erro de valor')
    except NameError:
        print('Erro de nome')
    else:
        print(f'Operação bem sucedida, divisão {int(v)}')
        break
    finally:
        print('')