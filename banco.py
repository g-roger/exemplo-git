def sacar(saldo, valor_de_saque):
    if valor_de_saque >= 0:
        return saldo - valor_de_saque


def depositar(saldo, valor_de_deposito):
    if valor_de_deposito <= 1000:
        return saldo + valor_de_deposito
    return saldo


def extrato(saldo):
    print('Extrato:-----', saldo)


def executar_atm():
    saldo = float(input('digite um valor para simular seu saldo maior que 0-->'))
    opcao = 0
    
    while int(opcao) != 4:
        print('digite 1 para sacar')
        print('digite 2 para extrato')
        print('digite 3 para deposito')
        print('digite 4 para finalizar')

        opcao = input('qual sua opcao? ')
        
        if int(opcao) == 1:
            valor_saque = float(input('Qual seu valor de saque? '))
            print(sacar(saldo, valor_saque))
        elif int(opcao) == 2:
            extrato()
        elif int(opcao) == 3:
            valor_deposito = float(input('Qual seu valor de deposito? '))
            print(sacar(saldo, valor_deposito))
        else:
            print("Opção inválida. Tente novamente.")
