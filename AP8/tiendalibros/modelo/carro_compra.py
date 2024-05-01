from item_compra import ItemCompra  # Importamos la clase ItemCompra

class CarroCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, libro, cantidad):
        item = ItemCompra(libro, cantidad)  # Creamos un nuevo objeto ItemCompra
        self.items.append(item)  # Agregamos el item a la lista de items
        return item  # Retornamos el item creado

    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total
