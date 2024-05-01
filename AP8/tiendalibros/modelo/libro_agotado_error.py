from tiendalibros.modelo.libro_error import LibroError


class LibroError(Exception):
    pass

class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__(f"El libro con titulo '{titulo}' y isbn '{isbn}' esta agotado")

    def __str__(self):
        return self.args[0]
