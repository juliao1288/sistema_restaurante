class Pilha:

    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if self.isEmpty():
            print("Erro ao remover. Não há elementos na pilha")

        return self._elementos.pop()
        
    def isEmpty(self):
        if len(self._elementos) == 0:
            return True

        return False

    def top(self):
        if self.isEmpty():
            return None
        
        return self._elementos[-1]
    
    def size(self):
        return len(self._elementos)
