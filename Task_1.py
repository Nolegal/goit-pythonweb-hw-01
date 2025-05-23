from abc import ABC, abstractmethod
import logging



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass



class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f" {self.make} {self.model} ({self.region_spec} Spec): Двигун запущено"
        )



class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f" {self.make} {self.model} ({self.region_spec} Spec): Мотор заведено"
        )



class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US")



class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU")



if __name__ == "__main__":

    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Cadillac", "Escalade") 
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "FLHR/I Road King")

    us_car.start_engine()
    us_motorcycle.start_engine()


    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("BMW", "X5")
    eu_motorcycle = eu_factory.create_motorcycle("Peugeot", "e-LUDIX")

    eu_car.start_engine()
    eu_motorcycle.start_engine()