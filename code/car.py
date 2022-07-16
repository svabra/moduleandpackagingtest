from code.elements.type_of_car import TypeOfCar

class Car():

    def __init__(self, type_of_car:TypeOfCar=TypeOfCar.UNIVERSAL) -> None:
        self.type_of_car: TypeOfCar = type_of_car

    def drive(self) -> str:        
        return "driving"

    def accelerate(self) -> str:
        return "accelerating"