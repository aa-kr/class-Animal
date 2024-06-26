class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} щебечет.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

###  Функция для демонстрации полиморфизма

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлен {animal.name} в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавлен {staff_member.name} в сотрудники зоопарка.")


class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

### Демонстрация

# Создаем животных
parrot = Bird("Попугай", 2, 25)
lion = Mammal("Лев", 5, "желтый")
snake = Reptile("Змея", 3, "гладкий")

# Создаем сотрудников
zookeeper = ZooKeeper("Иван")
vet = Veterinarian("Доктор Петров")

# Создаем зоопарк и добавляем в него животных и сотрудников
zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)
zoo.add_staff(zookeeper)
zoo.add_staff(vet)

# Демонстрируем полиморфизм
animal_sound(zoo.animals)

# Используем методы сотрудников
zookeeper.feed_animal(lion)
vet.heal_animal(snake)



