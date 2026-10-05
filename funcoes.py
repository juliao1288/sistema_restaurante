#Funções 
import fila
import pilha


def cadastrar_item(id: int, nome: str, preco: float):
    produto = {
        "id": id,
        "nome": nome,
        "preco": preco
    }

    return produto


def remover_item(cardapio, id: int):
    for produto in cardapio:
        if produto["id"] == id:
            cardapio.remove(produto)
            return True

    return False
