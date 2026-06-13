'''
Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
свойство "тип кузова". 
'''
class Transport:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Car(Transport):
    def __init__(self, brand: str, model: str, year: int, body_type: str):
        super().__init__(brand, model, year)
        self.body_type = body_type

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Body Type: {self.body_type}")

car1 = Car("Toyota", "Camry", 2022, "Sedan")
car1.display_info()

car2 = Car("BMW", "X5", 2024, "SUV")
car2.display_info()