class Fila:
    
    def __init__(self):
        self._pedidos = []

    def enqueue(self, pedido):
        self._pedidos.append(pedido)

    def dequeue(self):
        if not self.isEmpty():
            return self._pedidos.pop(0)
        return None
    
    def size(self):
        return len(self._pedidos)
    
    def isEmpty(self):
        return len(self._pedidos) == 0
    
    def front(self):
        if not self.isEmpty():
            return self._pedidos[0]
        return None
    
    def ver_fila(self):
        print(self._pedidos)
