class Animal:
    def __init__(self, name, kingdom, phylum, animal_class, order, family, genus, scientific_name):
        self.name = name
        self.kingdom = kingdom
        self.phylum = phylum
        self.animal_class = animal_class
        self.order = order
        self.family = family
        self.genus = genus
        self.scientific_name = scientific_name
    
    def __repr__(self):
        return f"<Animal(name={self.name}, scientific_name={self.scientific_name})>"