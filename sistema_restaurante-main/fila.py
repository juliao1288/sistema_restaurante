class Fila:
    
    def __init__(self):
        self._pedidos = []

    def lançar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def atender_pedido(self):
        if not self.isEmpty():
            return self._pedidos.pop(0)
        return None
    
    def size(self):
        return len(self._pedidos)
    
    def isEmpty(self):
        return len(self._pedidos) == 0
    
    def ver_proximo_pedido(self):
        if not self.isEmpty():
            return self._pedidos[0]
        return None
    
    def ver_fila(self):
        print(self._pedidos)
