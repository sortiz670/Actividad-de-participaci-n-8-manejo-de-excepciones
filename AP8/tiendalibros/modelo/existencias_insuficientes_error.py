from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias):
        mensaje = (f"El libro con titulo '{titulo}' y isbn '{isbn}' "
                   f"no tiene suficientes existencias para realizar la compra: "
                   f"cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}")
        super().__init__(mensaje)
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return self.args[0]
