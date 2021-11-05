print ("\t CONVERSOR DE MEDIDA \n")
x = float(input("Digite uma medida: "))

y = 0
while y == 0:
    print(" [1] Km \n [2] Hm \n [3] Dam \n [4] M \n [5] Dm \n [6] Cm \n [7] Mm \n [8] Fechar o programa")
    z = int(input("\n Escolha uma opção: "))
    if z == 1:
        print(" [1] KM para Hm "
              "\n [2] KM para Dam "
              "\n [3] KM para M "
              "\n [4] KM para Dm "
              "\n [5] KM para Cm "
              "\n [6] KM para Mm "
              "\n [7] Voltar ao inicio "
              "\n [8] Fechar programas")
        K_m = int(input('\n Escolha uma opção: '))
        if K_m == 1:
            K_H = x * 10
            print('O seu valor em {}Km convertido em {}Hm'.format(x, K_H))
            exit(' \n Fim do cod')
        if K_m == 2:
            K_Da = x * 100
            print('O seu valor em {}Km convertido em {}Dam'.format(x, K_Da))
            exit(' \n Fim do cod')
        if K_m == 3:
            K_M = x * 1000
            print('O seu valor em {}Km convertido em {}M'.format(x, K_M))
            exit(' \n Fim do cod')
        if K_m == 4:
            K_d = x * 10000
            print('O seu valor em {}Km convertido em {}Dm'.format(x, K_d))
            exit(' \n Fim do cod')
        if K_m == 5:
            K_c = x * 100000
            print('O seu valor em {}Km convertido em {}Cm'.format(x, K_c))
            exit(' \n Fim do cod')
        if K_m == 6:
            K_MM = x * 1000000
            print('O seu valor em {}Km convertido em {}Mm'.format(x, K_MM))
            exit(' \n Fim do cod')
        if K_m == 7:
            print(z)
        if K_m == 8:
            print('Fechando programa.....')
            exit('FIM')
    if z == 2:
        print(" [1] Hm para Km \n"
              " [2] Hm para Dam \n"
              " [3] Hm para M \n"
              " [4] Hm para Dm \n"
              " [5] Hm para Cm \n"
              " [6] Hm para Mm \n"
              " [7] De volta ao inicio \n"
              " [8] Fechar programa")
        HM = int(input(' \n Escolha uma opção'))
        if HM == 1:
            H_k = x / 10
            print('Sua medida em {}Hm convertida em {}Km'.format(x, H_k))
            exit('Fim do cod')
        if HM == 2:
            H_Da = x * 10
            print('Sua medida em {}Hm convertida em {}Dam'.format(x, H_Da))
            exit('Fim do cod')
        if HM == 3:
            H_m = x * 100
            print('Sua medida em {}Hm convertida em {}M'.format(x, H_m))
            exit('Fim do cod')
        if HM == 4:
            H_dm = x * 1000
            print('Sua medida em {}Hm convertida em {}Dm'.format(x, H_dm))
            exit('Fim do cod')
        if HM == 5:
            H_cm = x * 10000
            print('Sua medida em {}Hm convertida em {}Cm'.format(x, H_cm))
            exit('Fim do cod')
        if HM == 6:
            H_mm = x * 100000
            print('Sua medida em {}Hm convertida em {}Mm'.format(x, H_mm))
            exit('Fim do cod')
        if HM == 7:
            print(z)
        if HM == 8:
            print("\t Fechando programa...")
            exit('Fim')
    if z == 3:
        print('  [1] Dam para Km '
              '\n [2] Dam para Hm '
              '\n [3] Dam para M '
              '\n [4] Dam para Dm '
              '\n [5] Dam para Cm '
              '\n [6] Dam para Mm '
              '\n [7] Voltar ao inicio '
              '\n [8] Fechar o programa')
        DAM = int(input('\n Escolha sua opção: '))
        if DAM == 1:
            Da_k = x / 100
            print('Sua medida em {}Dam convertida em {}Km'.format(x, Da_k))
            exit('Fim do programa')
        if DAM == 2:
            Da_h = x / 10
            print('Sua medida em {}Dam convertida em {}Hm'.format(x, Da_h))
            exit('Fim do programa')
        if DAM == 3:
            Da_m = x * 10
            print('Sua medida em {}Dam convertida em {}M'.format(x, Da_m))
            exit('Fim do programa')
        if DAM == 4:
            Da_d = x * 100
            print('Sua medida em {}Dam convertida em {}Dm'.format(x, Da_d))
            exit('Fim do programa')
        if DAM == 5:
            Da_c = x * 1000
            print('Sua medida em {}Dam convertida em {}Cm'.format(x, Da_c))
            exit('Fim do programa')
        if DAM == 6:
            Da_M = x * 10000
            print('Sua medida em {}Dam convertida em {}Mm'.format(x, Da_M))
            exit('Fim do programa')
        if DAM == 7:
            print(z)
        if DAM == 8:
            print('\t Fim do programa....')
            exit('Fim do programa')
    if z == 4:
        print(' [1] M para Km '
              '\n [2] M para Hm '
              '\n [3] M para DAm '
              '\n [4] M para Dm '
              '\n [5] M para Cm '
              '\n [6] M para Mm '
              '\n [7] Voltar ao inicio '
              '\n [8] Fechar programa')
        M = int(input('\n Escolha uma opção'))
        if M == 1:
            M_k = x / 1000
            print('A sua medida {}M convertida em {}Km'.format(x, M_k))
            exit('Fim do programa')
        if M == 2:
            M_h = x / 100
            print('A sua medida {}M convertida em {}Hm'.format(x, M_h))
            exit('Fim do programa')
        if M == 3:
            M_da = x / 10
            print('A sua medida {}M convertida em {}DAm'.format(x, M_da))
            exit('Fim do programa')
        if M == 4:
            M_d = x * 10
            print('A sua medida {}M convertida em {}Dm'.format(x, M_d))
            exit('Fim do programa')
        if M == 5:
            M_c = x * 100
            print('A sua medida {}M convertida em {}Cm'.format(x, M_c))
            exit('Fim do programa')
        if M == 6:
            M_m = x * 1000
            print('A sua medida {}M convertida em {}Mm'.format(x, M_m))
            exit('Fim do programa')
        if M == 7:
            print(z)
        if M == 8:
            print('Fechando programa........')
            exit('Fim do programa')
    if z == 5:
        print(' [1] Dm para Km '
              '\n [2] Dm para Hm '
              '\n [3] Dm para Dam '
              '\n [4] Dm para M '
              '\n [5] Dm para Cm '
              '\n [6] Dm para Mm '
              '\n [7] Voltar ao inicio '
              '\n [8] Fechar o programa')
        DM = int(input('\n escolha uma opção: '))
        if DM == 1:
            D_k = x / 10000
            print('A sua medida em {]Dm convertida em {}Km'.format(x, D_k))
            exit('Fim do programa')
        if DM == 2:
            D_h = x / 1000
            print('A sua medida em {]Dm convertida em {}Hm'.format(x, D_h))
            exit('Fim do programa')
        if DM == 3:
            D_da = x / 100
            print('A sua medida em {]Dm convertida em {}DAm'.format(x, D_da))
            exit('Fim do programa')
        if DM == 4:
            D_m = x / 10
            print('A sua medida em {]Dm convertida em {}M'.format(x, D_m))
            exit('Fim do programa')
        if DM == 5:
            D_c = x * 10
            print('A sua medida em {]Dm convertida em {}Cm'.format(x, D_c))
            exit('Fim do programa')
        if DM == 6:
            D_m = x * 100
            print('A sua medida em {]Dm convertida em {}Mm'.format(x, D_m))
            exit('Fim do programa')
        if DM == 7:
            print(z)
        if DM == 8:
            print('Finalizando programa........')
            exit('Fim do programa')
    if z == 6:
        print(' [1] Cm para Km \n'
              ' [2] Cm para Hm \n'
              ' [3] Cm para Dam \n'
              ' [4] Cm para M \n'
              ' [5] Cm para Dm \n'
              ' [6] Cm para Mm \n'
              ' [7] Voltar ao inicio \n'
              ' [8] Fechar o programa')
        CM = int(input('\n Escolha sua opção: '))
        if CM == 1:
            C_k = x / 100000
            print('A sua medida {}Cm convertida em {}Km'.format(x, C_k))
            exit('Fim do programa')
        if CM == 2:
            C_h = x / 10000
            print('A sua medida {}Cm convertida em {}Hm'.format(x, C_h))
            exit('Fim do programa')
        if CM == 3:
            C_da = x / 1000
            print('A sua medida {}Cm convertida em {}DAm'.format(x, C_da))
            exit('Fim do programa')
        if CM == 4:
            C_m = x / 100
            print('A sua medida {}Cm convertida em {}M'.format(x, C_m))
            exit('Fim do programa')
        if CM == 5:
            C_d = x / 10
            print('A sua medida {}Cm convertida em {}Dm'.format(x, C_d))
            exit('Fim do programa')
        if CM == 6:
            C_mm = x * 10
            print('A sua medida {}Cm convertida em {}Mm'.format(x, C_mm))
            exit('Fim do programa')
        if CM == 7:
            print(z)
        if CM == 8:
            print('Fechando programa........')
            exit('Fechando programa')
    if z == 7:
        print(' [1] Mm para Km \n'
              ' [2] Mm para Hm \n'
              ' [3] Mm para Dam \n'
              ' [4] Mm para M \n'
              ' [5] Mm para Dm \n'
              ' [6] Mm para Cm \n'
              ' [7] Voltar ao inicio \n'
              ' [8] Fechar o programa')
        MM = int(input('\n Escolha uma opção: '))
        if MM == 1:
            M_k = x / 1000000
            print('Sua medida {}Mm convertida em {}Km'.format(x, M_k))
            exit('Fechando programa')
        if MM == 2:
            M_h = x / 100000
            print('Sua medida {}Mm convertida em {}Hm'.format(x, M_h))
            exit('Fechando programa')
        if MM == 3:
            M_da = x / 10000
            print('Sua medida {}Mm convertida em {}DAm'.format(x, M_da))
            exit('Fechando programa')
        if MM == 4:
            M_m = x / 1000
            print('Sua medida {}Mm convertida em {}M'.format(x, M_m))
            exit('Fechando programa')
        if MM == 5:
            M_d = x / 100
            print('Sua medida {}Mm convertida em {}Dm'.format(x, M_d))
            exit('Fechando programa')
        if MM == 6:
            M_c = x / 10
            print('Sua medida {}Mm convertida em {}Cm'.format(x, M_c))
            exit('Fechando programa')
        if MM == 7:
            print(z)
        if MM == 8:
            print('Fechando programa..............')
            exit('Programa fechado')
    if z == 8:
        print('Fechando....')
        exit()