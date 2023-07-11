depositado = []
extrato_saque = []
saldo = 0
saque = 0


import time

print('Bem vindo(a) ao nosso sistema de caixa eletrônico')
while True:
    
    print('-'*40)
    menu = int(input('''             MENU
        SELECIONE A OPÇÃO DESEJADA
    [ 1 ] Saque
    [ 2 ] Depósito
    [ 3 ] Extrato
    [ 4 ] Saldo
    [ 0 ] Sair
    '''))
    print('-'*40)
    time.sleep(1)
    
    if menu == 1:
        if saque < 3:
            valor_saque = float(input('Digite o valor a ser sacado:\nR$'))
            
            while valor_saque > 500:
                print('Seu limite de saque é de R$500')
                valor_saque = float(input('Digite o valor a ser sacado:\nR$'))

            if valor_saque < 500 and valor_saque <= saldo:
                print('Realizando seu saque')
                saque += 1
                extrato_saque.append(valor_saque)
                saldo -= valor_saque
                time.sleep(1)
                print('Saque realizado com sucesso')


            elif valor_saque > saldo:
                print('Saldo insuficiente para relizar saque')

        else:
            print('Você já realizou 3 saques diarios')

    

    elif menu == 2:
        valor_depositado = float(input('Informe o valor q deseja depositar:\nR$'))
        if valor_depositado > 0:
            depositado.append(valor_depositado)
            saldo += valor_depositado
            time.sleep(1)
            print('Valor depositado com sucesso')
        else:
            print('Não é possivel depositar valor negativo')
        #print(f'{saldo}')
    
        

    elif menu == 3:
        print(f'Seu extrato de deposito {depositado:.2f}\nSeu extrato de saque {extrato_saque:.2f}\nSeu saldo atual é R${saldo:.2f}')

    elif menu == 4:
        print(f'Seu saldo atual é R${saldo:.2f}')

    elif menu == 0:
        break
    else:
        print('Digite uma opção valida.')
        
print(f'FIM')
