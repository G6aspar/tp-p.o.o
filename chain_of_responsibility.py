class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor is not None:
            self._successor.handle(request)

class AnimalNameValidator(Handler):
    def handle(self, name):
        if not name.isalpha():
            raise ValueError(f"Nombre de animal no válido: '{name}'.")
        super().handle(name)

class AnimalDataFormatter(Handler):
    def handle(self, data):
        super().handle(data)
