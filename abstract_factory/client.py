"Abstract Factory Use Case Example Code"
from furniture_factory import FurnitureFactory


FURNITURE = FurnitureFactory.get_furniture("SmallChair")
if FURNITURE is not None :
    print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")

FURNITURE = FurnitureFactory.get_furniture("MediumTable")
if FURNITURE is not None :
    print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")
