from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        return "Woof!"
class cat(Animal):
    def sound(self):
        return "Meow"

# objanimal = Animal()
objdog = dog()
print(objdog.sound())