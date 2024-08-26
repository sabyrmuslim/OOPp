class Dog:
    def __init__(self, name, age, breed, hunger=50, energy=50):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.energy = energy
        self.breed = breed
    

    def dark(self):
        print(f"{self.name} говорит: Гав! ")

    def eat(self):
        self.hunger += 10
        self.energy -= 5
        print(f"{self.name}, поел теперь он сытый")

    def sleep(self):
        self.hunger -= 5
        self.energy += 10
        print(f"{self.name}, поспал и теперь полон энергии")

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.hunger -= 5
            print(f"{self.name}, поиграл и повеселился и устал")
        else:
            print(f"{self.name} слишком устал чтобы играть, (пусть поспит)")

    def status(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Сытость: {self.hunger}")
        print(f"Энергия: {self.energy}")
        print(f"Парода: {self.breed}")


class WorkingDog(Dog):
    def __init__(self, name, age, breed, job, hunger=50, energy=50):
        super().__init__(name, age, breed, hunger, energy)
        self.job = job

    def perform_job(self):
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} выполняет свою работу! ОХРАНА!!!")
        else:
            print(f"{self.name} слишком устал чтобы работать ")

    def status(self):
        super().status()
        print(f"Работа: {self.job}")


my_dog = Dog("Бобик", 3, "Тайган")
working_dog = WorkingDog("Рекс", 4, "Немецкая овчарка", "Охрана")

while True:
    print("Что сделать с собакой? ")
    print("1. Погладить ")
    print("2. Покормить ")
    print("3. Поспать ")
    print("4. Поиграть ")
    print("5. Проверить статус ")
    print("6. Выполнить работу (для служебной собаки)")
    print("7. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        my_dog.dark()
    elif choice == "2":
        my_dog.eat()
        working_dog.eat()
    elif choice == "3":
        my_dog.sleep()
        working_dog.sleep()
    elif choice == "4":
        my_dog.play()
        working_dog.play()
    elif choice == "5":
        my_dog.status()
        working_dog.status()
    elif choice == "6":
        working_dog.perform_job()
    elif choice == "7":
        print("Заходи еще поиграть мы тебя ждем!!!")
        break
    else:
        print("Некорректный ввод, собака обиделась на тебя ...")
