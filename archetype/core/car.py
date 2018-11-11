from abc import ABC, abstractmethod
from enum import Enum, auto


class CarMake(Enum):
    """
    Enumeration https://docs.python.org/3/library/enum.html

    auto() just assigns an empty object to the enum member, since on python every enum member must have a value.
    """
    KIA = auto()
    FIAT = auto()

class Car(ABC):
    """
    Abstract base class for a car entity (contract). Since python does not support interfaces
    for a contractual design. ABCs are the way to go.

    ABCs can not be instantiated! They are merely a contract!

    Abstract methods must be overwritten by subclasses.

    https://docs.python.org/3/library/abc.html
    """
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def make(self) -> CarMake:
        pass

    @abstractmethod
    def topspeed(self) -> int:
        pass


class Ceed(Car):
    def drive(self):
        print("brum brum")

    def make(self) -> CarMake:
        return CarMake.KIA

    def topspeed(self) -> int:
        return 210


class Pinto(Car):
    def drive(self):
        print("andiamo! brrrrrr")

    def make(self) -> CarMake:
        return CarMake.FIAT

    def topspeed(self) -> int:
        return 120



def run_example():
    ceed = Ceed()
    pinto = Pinto()
    ceed.drive()
    pinto.drive()

if __name__ == '__main__':
    run_example()