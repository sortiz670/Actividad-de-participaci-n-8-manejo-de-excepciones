from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__(f"El libro con titulo '{titulo}' y isbn: '{isbn}' ya existe en el catálogo")

    def __str__(self):
        return self.args[0]
    
    
