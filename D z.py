class SuperHero:
    def __init__(self, name, superpower, city):
        self.name = name
        self.superpower = superpower
        self.city = city       
        

    def introduce(self):
        print(f"Привет! Я {self.name}, моя суперспособность - {self.superpower}, я из города - {self.city}.")
        
        
SuperHero1 = SuperHero("Капитан Молния", "Управление электричеством", "Нью-Йорк")
SuperHero2 = SuperHero("Леди Ветер", "Управление ветром", "Токио")

SuperHero1.introduce()
SuperHero2.introduce()