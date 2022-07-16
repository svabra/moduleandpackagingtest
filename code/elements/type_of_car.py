from enum import Enum

class TypeOfCar(str, Enum):
    SEDAN = "Sedan"
    CONVERTIBLE = "Convertible"
    COUPE = "Coupé"
    HATCHBACK = "Hatchback"
    UNIVERSAL = "Universal"
    LIFTBACK = "Liftback"