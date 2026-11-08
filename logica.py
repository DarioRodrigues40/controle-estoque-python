estoque = []


def codigo_existe(codigo):
    return any(produto["codigo"] == codigo for produto in estoque)


def ler(mensagem, validacao, erro):
    valor = input(mensagem)
    if validacao(valor):
        return valor
    print(erro)
    return ler(mensagem, validacao, erro)


def cadastrar_produto():
    print("\n=== CADASTRO DE PRODUTO ===")

    codigo = ler(
        "Código do produto: ",
        lambda x: x.isdigit() and len(x) == 5 and not codigo_existe(x),
        "Código inválido!"
    )

    nome = ler(
        "Nome do produto: ",
        lambda x: x.replace(" ", "").isalpha(),
        "Nome inválido!"
    )

    preco = float(
        ler(
            "Preço do produto: ",
            lambda x: x.replace(".", "", 1).isdigit() and float(x) >= 0,
            "Preço inválido!"
        )
    )

    quantidade = int(
        ler(
            "Quantidade do produto: ",
            lambda x: x.isdigit(),
            "Quantidade inválida!"
        )
    )

    estoque.append({
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    })

    print("Produto cadastrado com sucesso!")


def calcular_total_produtos():
    if not estoque:
        print("\nNenhum produto cadastrado.")
        return

    print("\n=== PRODUTOS EM ESTOQUE ===")

    for produto in estoque:
        print(
            f"Código: {produto['codigo']}\n"
            f"Nome: {produto['nome']}\n"
            f"Preço: R$ {produto['preco']:.2f}\n"
            f"Quantidade: {produto['quantidade']}\n"
        )


def exibir_menu():
    print("\n===== CONTROLE DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Calcular total de produtos em estoque")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
        return exibir_menu()

    if opcao == "2":
        calcular_total_produtos()
        return exibir_menu()

    if opcao != "3":
        print("Opção inválida!")
        return exibir_menu()

    print("Sistema encerrado.")


exibir_menu()