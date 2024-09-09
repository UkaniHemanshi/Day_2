#Base class(Suprclass)
class Animal:

    def speak(self):
        print("Animal speaks")

#Derived class(Subclass) inherting from Animal
class Dog(Animal):
    def speak(self):
         print(f"says woof")

def make_animal_speak(animal):
        animal.speak()

dog = Dog()
make_animal_speak(dog)