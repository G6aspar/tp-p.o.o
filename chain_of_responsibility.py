class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor is not None:
            self._successor.handle(request)

class AnimalNameValidator(Handler):
    def handle(self, name):
        if not name.isalpha():
            raise ValueError(f"Invalid animal name: '{name}'.")
        super().handle(name)

class AnimalDataFormatter(Handler):
    def handle(self, data):
        # You could add any extra processing here, for now we pass it through
        super().handle(data)
