from dao.animal_dao import AnimalDao, CatDao, DogDao
from utils.chain_of_responsibility import AnimalNameValidator, AnimalDataFormatter
from exceptions.custom_exceptions import AnimalNotFoundException

class AnimalService:
    def __init__(self, dao):
        self.animal_dao = dao
        self.chain = AnimalNameValidator(AnimalDataFormatter())

    def fetch_animal_info(self, name):
        self.chain.handle(name)
        data = self.animal_dao.get_animal_data(name)
        if not data:
            raise AnimalNotFoundException(f"Animal '{name}' no encontrado.")
        return data

class CatService(AnimalService):
    def __init__(self):
        super().__init__(CatDao())

class DogService(AnimalService):
    def __init__(self):
        super().__init__(DogDao())

