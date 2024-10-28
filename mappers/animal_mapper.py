from models.animal import Animal

class AnimalMapper:
    def format_animal_data(raw_data):
        animals = []
        for animal in raw_data:
            animals.append(Animal(
                name=animal.get('name'),
                kingdom=animal.get('taxonomy', {}).get('kingdom'),
                phylum=animal.get('taxonomy', {}).get('phylum'),
                animal_class=animal.get('taxonomy', {}).get('class'),
                order=animal.get('taxonomy', {}).get('order'),
                family=animal.get('taxonomy', {}).get('family'),
                genus=animal.get('taxonomy', {}).get('genus'),
                scientific_name=animal.get('taxonomy', {}).get('scientific_name'),
            ))
        return animals