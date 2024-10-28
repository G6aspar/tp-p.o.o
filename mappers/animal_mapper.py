from exceptions.custom_exceptions import AnimalNotFoundException

class AnimalMapper:
    def format_animal_data(raw_data):
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