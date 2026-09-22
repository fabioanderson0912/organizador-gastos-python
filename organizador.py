transacoes = [] # Nossa lista global para guardar as transações

def exibir_menu():
    print("\n== ORGANIZADOR DE GASTOS ===")
    print("1. Adicionar transação")
    print("2. Ver saldo e extrato")
    print("3. Sair")
    print("4. Sobre o projeto")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Nova Transação ---")
            descricao = input("Descrição (ex: Salário, Aluguel):")

            # Tratamento de erro para o valor monetário
            try:
                valor = float(input("Valor (ex: 150.50): "))
            except ValueError:
                print("Erro: Digite apenas números válidos (ex: 150.50)!")
                continue # Cancela este cadastro e volta para o menu inicial

            tipo = input("Tipo ('receita' ou 'despesa'): ").lower()

            # Validação do tipo de transação
            if tipo not in ['receita', 'despesa']:
                print("Erro: O tipo deve ser obrigatoriamente 'receita' ou 'despesa'!" )
                continue
            
            transacao = {
                "descricao": descricao,
                "valor": valor,
                "tipo": tipo
            }
            transacoes.append(transacao)
            print("Transação cadastrada com sucesso!")

        elif opcao == "2":
            print("\n=== EXTRATO FINANCEIRO ===")
            if not transacoes:
                print("Nenhuma transação registrada ainda.")
            else:
                saldo = 0
                for t in transacoes:
                    print(f"- {t['descricao']}: R$ {t['valor']:.2f} ({t['tipo']})")
                    if t['tipo'] == 'receita':
                        saldo += t['valor']
                    elif t['tipo'] == 'despesa':
                        saldo -= t['valor']
                print(f"\nSaldo atual: R$ {saldo:.2f}")
        
        elif opcao == "3":
            print("Saindo do programa. Até mais!")
            break
        elif opcao == "4":
            print("Projeto desenvolvido por mim no meu portifólio!")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()