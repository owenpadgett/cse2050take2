class Foo:
    def __init__(self, name: str, profession: str) -> None:
        '''initialize new Foo object'''
        self.name = name
        self.profession = profession
    
    def __repr__(self) -> str:
        '''Allows useful printing of Foo objects'''
        return f"Foo({self.name}, {self.profession})"
    
    def speak(self):
        return f"{self.name} says hello!"