def sacar(saldo, valor_de_saque):
    if valor_de_saque >= 0:
        return saldo - valor_de_saque


def depositar(saldo, valor_de_deposito):
    if valor_de_deposito <= 1000:
        return saldo + valor_de_deposito
    return saldo


def extrato(saldo):
    print('Extrato:-----', saldo)
