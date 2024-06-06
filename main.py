def main():
    menu = """
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair

        => """

    deposito = 0
    saque = 0
    extrato = 0
    saque_total_dia = 500

    while True:
        opcao = input(menu)

        if opcao == '1':
            deposito += float(input("Insira o valor de depósito R$: "))
        elif opcao == '2':
            saque = float(input("Insira o valor do saque R$: "))
            if saque <= saque_total_dia:
                deposito -= saque
                saque_total_dia -= saque  # Atualiza o saque total do dia
            else:
                print("Valor de saque excede o limite diário.")
        elif opcao == '3':
            extrato = f"""
            Saldo Atual: R$ {deposito:.2f}
            Saque: R$ {saque:.2f}
            """
            print(extrato)
        else:
            break

if __name__ == "__main__":
    main()