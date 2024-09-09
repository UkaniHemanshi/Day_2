from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(f"car is started")
    def stop(self):
        print(f"car is stopped")

class Bike(Vehicle):
    def start(self):
        print(f"bike is started")
    def stop(self):
        print(f"bike is stopped")

class Bus(Vehicle):
    def start(self):
        print(f"bus is started")
    def stop(self):
        print(f"bus is stopped")


class garage:
    v_list = []
    def add_vehicle(self,*args):
         for i in args:
                self.v_list.append(i)
                print(i.__class__.__name__)
         # print(v_list)

    def operate_vehicle(self):
        for v in self.v_list:
            v.start()
            v.stop()

objgar = garage()


objcar = Car()
objbike = Bike()
objbus = Bus()

objgar.add_vehicle(objcar,objbike,objbus)
objgar.operate_vehicle()
print(len(objgar.v_list))
