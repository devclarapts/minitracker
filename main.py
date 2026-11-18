despesas = []


def adicionar_despesa():
    descricao = input("Descricao da despesa: ").strip()
    if descricao == "":
        print("A descricao nao pode ser vazia.")
        return

    texto_valor = input("Valor (ex: 25.50): ").strip().replace(",", ".")
    try:
        valor = float(texto_valor)
    except ValueError:
        print("Valor invalido. Digite um numero, por exemplo: 25.50")
        return

    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return

    categoria = input("Categoria (ex: alimentacao, transporte): ").strip()
    if categoria == "":
        print("A categoria nao pode ser vazia.")
        return

    despesas.append({
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    })
    print(f"Despesa adicionada: {descricao} - R$ {valor:.2f}")


def listar_despesas():
    if len(despesas) == 0:
        print("Nenhuma despesa cadastrada ainda.")
        return

    print("\nDespesas cadastradas:")
    numero = 1
    for despesa in despesas:
        print(f"{numero}. {despesa['descricao']} | R$ {despesa['valor']:.2f} | {despesa['categoria']}")
        numero += 1


def mostrar_total():
    if len(despesas) == 0:
        print("Nenhuma despesa cadastrada ainda.")
        return

    total = 0
    for despesa in despesas:
        total = total + despesa["valor"]
    print(f"Total de despesas: R$ {total:.2f}")


def mostrar_menu():
    print("\n--- Mini Expense Tracker ---")
    print("1 - Adicionar despesa")
    print("2 - Listar despesas")
    print("3 - Mostrar total")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            adicionar_despesa()
        elif opcao == "2":
            listar_despesas()
        elif opcao == "3":
            mostrar_total()
        elif opcao == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


main()
