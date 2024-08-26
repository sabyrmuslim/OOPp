class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_hero(self):
        return f'Hero name ==> {self.name}'

    def extra_health(self):
        self.health_points *= 2
        print(f"Здоровье героя увеличено до: {self.health_points}")

    def __str__(self):
        return (f"Прозвище {self.nickname}, суперспособность - {self.superpower},"
                f" здоровье - {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Брюс Бэннер", "Халк",
                 "Сила", 100, "Халк КРУШИТЬ!!!")
print(hero)
