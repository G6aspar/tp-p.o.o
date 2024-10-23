from dao.animal_dao import AnimalDao
from utils.chain_of_responsibility import AnimalNameValidator, AnimalDataFormatter
from exceptions.custom_exceptions import AnimalNotFoundException

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
        
        formatted_data = self.format_animal_data(raw_data)
        return formatted_data

    def format_animal_data(self, raw_data):
        formatted_data = []
        for animal in raw_data:
            formatted_data.append({
            'name': animal.get('name'),
            'taxonomy': {
                'kingdom': animal.get('taxonomy', {}).get('kingdom'),
                'phylum': animal.get('taxonomy', {}).get('phylum'),
                'class': animal.get('taxonomy', {}).get('class'),
                'order': animal.get('taxonomy', {}).get('order'),
                'family': animal.get('taxonomy', {}).get('family'),
                'genus': animal.get('taxonomy', {}).get('genus'),
                'scientific_name': animal.get('taxonomy', {}).get('scientific_name'),
            }
        })
        return formatted_data

