menu = '''
Escolha uma opção:
      
[1] Saque
[2] Deposito
[3] Extrato
[4] Sair
      
=>'''

lista = [1,2,3,4]
saque = 0.0
limSaq = 3
saqFeito = 0
saldo = 0.0
valor = 0

#pensar no que por no break#

while True:

    op = int(input(menu))

    if op == 1 and limSaq !=0:
        saque = int(input("\nQual valor deseja sacar? "))

        if saque > 500:
            print ("\nSaque máximo permitido é de R$ 500,00")

        elif saque <= 500 and saldo >= 500:
            saldo -= saque
            limSaq -= 1
            print(f'''\nAqui está seu saque. \nSeu novo saldo é de {saldo:.2f}''')

        elif saque <= 500 and saldo < 500:
            print("\nVocê não tem saldo suficiente para esse saque, tente novamente")

    elif op ==1 and limSaq == 0:
        print("\nVocê não tem mais saques disponíveis para hoje")

    elif op == 2:
        valor = float(input("\nQual valor irá depositar? "))

        if valor > 0:
            saldo += valor
            print(f"\nSeu novo saldo é R$ {saldo:.2f}")

        else:
            print("\nDigite um valor válido")

    elif op == 3:
        print(f"\nSeu saldo é R$ {saldo:.2f}")
        
    elif op == 4:
        print("\nObrigado por usar nosso banco")
        break

    elif op not in lista:
        print("\nOpção inválida, digite novamente o que deseja fazer")
