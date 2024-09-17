class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if self.esta_vazia():
            return "A fila está vazia."
        return self.itens.pop(0)

    def primeiro(self):
        if self.esta_vazia():
            return "A fila está vazia."
        return self.itens[0]

    def tamanho(self):
        return len(self.itens)


# Uso
fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print("Primeiro da fila:", fila.primeiro())  
print("Desenfileirado:", fila.desenfileirar()) 
print("Tamanho da fila:", fila.tamanho()) 
