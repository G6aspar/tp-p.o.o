from models.animal import Animal
from builders.animal_builder import AnimalBuilder 

class AnimalMapper:
    @staticmethod
    def format_animal_data(raw_data):
        animals = []
        for animal in raw_data:
            builder = AnimalBuilder()  
            formatted_animal = builder \
                .set_name(animal.get('name')) \
                .set_kingdom(animal.get('taxonomy', {}).get('kingdom')) \
                .set_phylum(animal.get('taxonomy', {}).get('phylum')) \
                .set_animal_class(animal.get('taxonomy', {}).get('class')) \
                .set_order(animal.get('taxonomy', {}).get('order')) \
                .set_family(animal.get('taxonomy', {}).get('family')) \
                .set_genus(animal.get('taxonomy', {}).get('genus')) \
                .set_scientific_name(animal.get('taxonomy', {}).get('scientific_name')) \
                .build()

            animals.append(formatted_animal)
        return animals
