#Funções 
import fila
import pilha


def registrar_historico(pilha_historico, pedido, acao):
    registro = {
        "acao": acao,
        "pedido": pedido
    }
    pilha_historico.push(registro)
    
def desfazer(pilha_historico, fila_cozinha):
    if pilha_historico.isEmpty():
        print("O histórico está vazio.")
        return
        
    ultima_acao = pilha_historico.pop()
    
    if ultima_acao["acao"] == "atender":
        fila_aux = classe.Fila()
        
        fila_aux.enqueue(ultima_acao["pedido"])
        
        while not fila_cozinha.isEmpty():
            fila_aux.enqueue(fila_cozinha.dequeue())
            
        while not fila_aux.isEmpty():
            fila_cozinha.enqueue(fila_aux.dequeue())
        
    elif ultima_acao["acao"] == "lancar":
        fila_aux = classe.Fila()
        while not fila_cozinha.isEmpty():
            pedido = fila_cozinha.dequeue()
            if pedido["id"] != ultima_acao["pedido"]["id"]:
                fila_aux.enqueue(pedido)
        while not fila_aux.isEmpty():
            fila_cozinha.enqueue(fila_aux.dequeue())
            
