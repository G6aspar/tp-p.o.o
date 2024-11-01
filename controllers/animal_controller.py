from services.animal_service import AnimalService
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
            animals = self.animal_service.fetch_animal_info(name)
            return animals
        except AnimalNotFoundException as e:
            raise e  

