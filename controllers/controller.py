from services.service import AnimalService
from exceptions.custom_exceptions import AnimalNotFoundException

class AnimalController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnimalController, cls).__new__(cls)
            cls._instance.animal_service = AnimalService()
        return cls._instance

    def get_animal_info(self, name):
        try:
            # Intenta obtener la información del animal
            animal_info = self.animal_service.fetch_animal_info(name)
            return animal_info
        except AnimalNotFoundException as e:
            # Maneja la excepción en caso de que el animal no sea encontrado
            raise e  # Puedes lanzar la excepción o manejarla como desees

