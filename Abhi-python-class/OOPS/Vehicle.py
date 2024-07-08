class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(self.make)
        print(self.model)

class Car(Vehicle):
    def __init__(self, make, model, fuelType):
        super().__init__(make, model) # calling parent class specific constructor block from child class contructer block using super() function
        self.fuelType = fuelType

    def display_info(self):
        print(self.make)
        print(self.model)
        print(self.fuelType)

C1 = Car("1", "2", "3")
C1.display_info()