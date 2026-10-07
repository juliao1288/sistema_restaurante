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
