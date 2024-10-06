from dao import AnimalDao
from chain_of_responsibility import AnimalNameValidator, AnimalDataFormatter
from exceptions import AnimalNotFoundException

class AnimalService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnimalService, cls).__new__(cls)
            cls._instance.animal_dao = AnimalDao()
            cls._instance.chain = AnimalNameValidator(AnimalDataFormatter())
        return cls._instance

    def fetch_animal_info(self, name):
        # Chain of Responsibility pattern to validate and process
        self.chain.handle(name)
        
        data = self.animal_dao.get_animal_data(name)
        if not data:
            raise AnimalNotFoundException(f"Animal '{name}' not found.")
        
        return data
