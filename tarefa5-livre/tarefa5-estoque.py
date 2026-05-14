def exibir_menu():
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar quantidade")
    print("5 - Calcular valor total do estoque")
    print("0 - Sair")


def ler_opcao():
    opcao = int(input("Escolha uma opção: "))
    return opcao


def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço unitário: R$ "))

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso.")


def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- LISTA DE PRODUTOS ---")

    for i, produto in enumerate(produtos):
        print(f"\nCódigo: {i}")
        print(f"Produto: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço unitário: R$ {produto['preco']:.2f}")


def encontrar_produto(produtos, nome_busca):
    for i, produto in enumerate(produtos):
        if produto["nome"].lower() == nome_busca.lower():
            return i

    return -1


def buscar_produto(produtos):
    nome_busca = input("Digite o nome do produto para buscar: ")

    posicao = encontrar_produto(produtos, nome_busca)

    if posicao == -1:
        print("Produto não encontrado.")
    else:
        produto = produtos[posicao]

        print("\nProduto encontrado:")
        print(f"Produto: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço unitário: R$ {produto['preco']:.2f}")


def atualizar_quantidade(produtos):
    nome_busca = input("Digite o nome do produto: ")

    posicao = encontrar_produto(produtos, nome_busca)

    if posicao == -1:
        print("Produto não encontrado.")
    else:
        nova_quantidade = int(input("Nova quantidade: "))
        produtos[posicao]["quantidade"] = nova_quantidade

        print("Quantidade atualizada com sucesso.")


def calcular_valor_total(produtos):
    total = 0

    for produto in produtos:
        total += produto["quantidade"] * produto["preco"]

    return total


def executar_sistema():
    produtos = []

    opcao = -1

    while opcao != 0:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == 1:
            cadastrar_produto(produtos)

        elif opcao == 2:
            listar_produtos(produtos)

        elif opcao == 3:
            buscar_produto(produtos)

        elif opcao == 4:
            atualizar_quantidade(produtos)

        elif opcao == 5:
            valor_total = calcular_valor_total(produtos)
            print(f"Valor total do estoque: R$ {valor_total:.2f}")

        elif opcao == 0:
            print("Encerrando o sistema...")

        else:
            print("Opção inválida.")


executar_sistema()
