from dao.animal_dao import AnimalDao
from utils.chain_of_responsibility import AnimalNameValidator, AnimalDataFormatter
from exceptions.custom_exceptions import AnimalNotFoundException
from mappers.animal_mapper import AnimalMapper

class AnimalService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnimalService, cls).__new__(cls)
            cls._instance.animal_dao = AnimalDao()
            cls._instance.chain = AnimalNameValidator(AnimalDataFormatter())
        return cls._instance

    def fetch_animal_info(self, name):
        self.chain.handle(name)
        
        raw_data = self.animal_dao.get_animal_data(name)
        if not raw_data:
            raise AnimalNotFoundException(f"Animal '{name}' no encontrado.")
        
        animals = AnimalMapper.format_animal_data(raw_data)
        return animals


