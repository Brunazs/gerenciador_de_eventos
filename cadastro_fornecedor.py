def cadastro_fornecedor():
    fornecedor = {
        "nome": input("Nome do fornecedor: "),
        "endereco": input("Endereço: "),
        "telefone": input("Telefone: "),
        "email": input("E-mail: ")
    }

    if not fornecedor["nome"].strip():
        print("O campo nome é obrigatório.")
        return

    else:
        fornecedores = []
    fornecedores.append(fornecedor)
    print(f"Fornecedor {fornecedor['nome']}, foi cadastrado com sucesso")
