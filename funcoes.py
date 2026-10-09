#Funções 
import fila
import pilha

#Funções padrão de verificação
def verificar_preco(preco):
    try:
        valor = float(str(preco).replace(',', '.'))
        return valor > 0
    except ValueError:
        return False
        
#RF01
def cadastrar_item(id: int, nome: str, preco: float):
    produto = {
        "id": id,
        "nome": nome,
        "preco": preco
    }

    return produto

#RF02
def remover_item(cardapio, id: int):
    for produto in cardapio:
        if produto["id"] == id:
            cardapio.remove(produto)
            print(" Produto removido com sucesso!")
            return True

    return False

#RF03
def visualizar_cardapio(cardapio):
    if not cardapio:
        print(" O cardápio está vazio.")
        return

    print(" -- CARDÁPIO -- ")
    for item in cardapio:
        print(f"ID: {item['id']} -- Nome: {item['nome']} -- Preço: R${item['preco']:.2f}")

# RF04 - Cadastrar Pedido
def cadastrar_pedido(cardapio, id_pedido):
    if not cardapio:
        print(" O cardápio está vazio. Não é possível lançar pedidos.")
        return None

    nome_cliente = input(" Qual o nome do cliente que deseja fazer o pedido? ").strip()
    lista_itens = []

    while True:
        
        while True:
            try:
                produto_selecionado = int(input(" Qual o ID do produto a ser comprado? "))
                break
            except ValueError:
                print(" Valor inválido! Digite apenas números.")

       
        exist = False
        for produto in cardapio:
            if produto["id"] == produto_selecionado:
                lista_itens.append(produto_selecionado)
                exist = True
                print("=" * 15)
                print(f" O item '{produto['nome']}' (ID: {produto_selecionado}) foi adicionado ao pedido de {nome_cliente}.")
                print("=" * 15)
                break

        if not exist:
            print(" Este ID não corresponde a nenhum produto no cardápio!")

        
        print("=" * 45)
        print("--- OPÇÕES LANÇAMENTO PEDIDO ---")
        print(" 1. Adicionar novo item ao pedido")
        print(" 2. Encerrar pedido")
        
        opcao = ""
        while opcao not in ["1", "2"]:
            opcao = input(" Escolha uma opção (1/2): ").strip()

        if opcao == "1":
            continue  
        elif opcao == "2":
            if not lista_itens:
                print("=" * 30)
                print(" O pedido não foi computado pois nenhum item foi adicionado.")
                print("=" * 30)
                return None
            else:
                pedido = {
                    "id": id_pedido,
                    "cliente": nome_cliente,
                    "itens": lista_itens
                }
                print(" Pedido encaminhado para a fila da cozinha!")
                return pedido


# RF05 
def realizar_pedido(pedido):
    if not pedido:
        print(" Não há pedidos a serem atendidos.")
        return False

    nome = pedido["cliente"]
    itens = pedido["itens"]
    
    descritivo = f"""
        ID DO PEDIDO  : #{pedido['id']}
        NOME CLIENTE  : {nome}
        IDs DOS ITENS : {itens}
    """

    print("----- PRIMEIRO PEDIDO DA FILA -----")
    print(descritivo)
    print(" 1. Definir esse pedido como realizado")
    print(" 2. Voltar ao menu principal")
    print("-" * 30)

    while True:
        try:
            opcao = int(input(" Escolha uma opção: "))
            print("-" * 30)
            
            match opcao:
                case 1:
                    print(" PEDIDO REALIZADO COM SUCESSO!")
                    print("-" * 15)
                    return True
                case 2:
                    return False
                case _:
                    print(" Opção inválida! Tente novamente.")
        except ValueError:
            print(" Entrada inválida! Digite 1 ou 2.")


#RF06
def visualizar_fila(fila_cozinha):
    if fila_cozinha.isEmpty():
        print(" A fila da cozinha está vazia!")
        return

    fila_aux = fila.Fila()

    print("=" * 45)
    print("         FILA DE PEDIDOS DA COZINHA")
    print("=" * 45)

  
    posicao = 1
    while not fila_cozinha.isEmpty():
        pedido = fila_cozinha.dequeue()
        
       
        print(f"Posição {posicao}º | Pedido #{pedido['id']} - Cliente: {pedido['cliente']}")
        print(f"   Itens (IDs): {pedido['itens']}")
        print("-" * 45)
        
        fila_aux.enqueue(pedido)
        posicao += 1

    
    while not fila_aux.isEmpty():
        fila_cozinha.enqueue(fila_aux.dequeue())
  
#RF07
def registrar_historico(pilha_historico, pedido, acao):
    registro = {
        "acao": acao,
        "pedido": pedido
    }
    pilha_historico.push(registro)

def visualizar_historico(pilha_historico):
    if pilha_historico.isEmpty():
        print(" O histórico de ações está vazio!")
        return

    pilha_aux = pilha.Pilha()

    print("=" * 45)
    print("      HISTÓRICO DE AÇÕES (Mais recente primeiro)")
    print("=" * 45)

   
    while not pilha_historico.isEmpty():
        registro = pilha_historico.pop()
        pedido = registro["pedido"]
        acao = registro["acao"].upper()

        print(f" Ação: [{acao}] | Pedido #{pedido['id']} - Cliente: {pedido['cliente']}")
        print("-" * 45)

        pilha_aux.push(registro)

   
    while not pilha_aux.isEmpty():
        pilha_historico.push(pilha_aux.pop())
    
#RF08    
def desfazer(pilha_historico, fila_cozinha):
    if pilha_historico.isEmpty():
        print("O histórico está vazio.")
        return
        
    ultima_acao = pilha_historico.pop()
    
    if ultima_acao["acao"] == "atender":
        fila_aux = fila.Fila()  
        
        fila_aux.enqueue(ultima_acao["pedido"])
        
        while not fila_cozinha.isEmpty():
            fila_aux.enqueue(fila_cozinha.dequeue())
            
        while not fila_aux.isEmpty():
            fila_cozinha.enqueue(fila_aux.dequeue())
            
        print(f" Ação desfeita: Pedido #{ultima_acao['pedido']['id']} voltou para a fila da cozinha!")
        
    elif ultima_acao["acao"] == "lancar":
        fila_aux = fila.Fila()  
        
        while not fila_cozinha.isEmpty():
            pedido = fila_cozinha.dequeue()
            if pedido["id"] != ultima_acao["pedido"]["id"]:
                fila_aux.enqueue(pedido)
                
        while not fila_aux.isEmpty():
            fila_cozinha.enqueue(fila_aux.dequeue())
            
        print(f" Ação desfeita: Lançamento do pedido #{ultima_acao['pedido']['id']} foi cancelado!")
