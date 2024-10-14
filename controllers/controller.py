from services.service import AnimalService, CatService, DogService
from dao.animal_dao import AnimalDao

class AnimalController:
    def __init__(self):
        self.animal_service = AnimalService(dao=AnimalDao())

    def get_animal_info(self, name):
        return self.animal_service.fetch_animal_info(name)

class CatController(AnimalController):
    def __init__(self):
        self.animal_service = CatService()

class DogController(AnimalController):
    def __init__(self):
        self.animal_service = DogService()

