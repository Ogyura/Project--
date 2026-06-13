'''
Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводит информацию о животном в формате "Имя: имя, Вид: вид".
'''
class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}")

animal1 = Animal("Barsik", "Cat")
animal1.display_info()

animal2 = Animal("Sharik", "Dog")
animal2.display_info()