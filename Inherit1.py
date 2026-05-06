from abc import ABC, abstractmethod

class Animal(ABC):
    def sound(self):
        print("Gutur gu... Animal")

class Bird(ABC):
    def sound(self):
        print("Koo... Koo...")
    @abstractmethod
    def fly():
        pass

class Pigeon(Bird,Animal):
    # def sound(self):
    #     print("Gutur gu...")
    def fly(self):
        print("Flying")

p = Pigeon()
p.sound()
p.fly()