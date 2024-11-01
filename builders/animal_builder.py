from models.animal import Animal

class AnimalBuilder:
    def __init__(self):
        self.name = None
        self.kingdom = None
        self.phylum = None
        self.animal_class = None
        self.order = None
        self.family = None
        self.genus = None
        self.scientific_name = None

    def set_name(self, name):
        self._name = name
        return self
    
    def set_kingdom(self, kingdom):
        self._kingdom = kingdom
        return self
    
    def set_phylum(self, phylum):
        self._phylum = phylum
        return self
    
    def set_animal_class(self, animal_class):
        self._animal_class = animal_class
        return self
    
    def set_order(self, order):
        self._order = order
        return self
    
    def set_family(self, family):
        self._family = family
        return self
    
    def set_genus(self, genus):
        self._genus = genus
        return self
    
    def set_scientific_name(self, scientific_name):
        self._scientific_name = scientific_name
        return self
    
    def build(self):
        return Animal(
            name=self._name,
            kingdom=self._kingdom,
            phylum=self._phylum,
            animal_class=self._animal_class,
            order=self._order,
            family=self._family,
            genus=self._genus,
            scientific_name=self._scientific_name,
        )
