class Animal:
    def __init__(self, name: str, species=None, sound='hi') -> None:
        '''Initializes Animal objects'''
        self.name = name
        self.sound = sound
        self.species = species

    def __repr__(self) -> str:
        '''Allows useful printing of Animal objects'''
        return f"Animal({self.name}, {self.species}, {self.sound})"
    
    def speak(self) -> str:
        '''Allows dogs to speak and say their name'''
        return f"{self.name}, a {self.species}, says {self.sound}!"
    
class Dog(Animal):
    def __init__(self, name: str, species='dog', sound='ruff', is_good_boy=True):
        '''Initializes Dog object'''
        self.name = name
        self.species = species
        self.sound = sound
        self.is_good_boy = is_good_boy

    def __repr__(self):
        '''Allows useful printing of Dog objects'''
        return f"Dog({self.name})"
    
class Cat(Animal):
    def __init__(self, name: str, species='Cat', sound='meow'):
        '''Initializes Cat object'''
        self.name = name
        self.species = species
        self.sound = sound

    def __repr__(self):
        '''Allows useful printing of Cat objects'''
        return f"Cat({self.name}, {self.species}, {self.sound})"