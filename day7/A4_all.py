from abc import ABC, abstractmethod

class Smartdevice(ABC):
    _name = ""
    _status = ""
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def device_info(self):
        pass

class Smartlight(Smartdevice):
    def turn_on(self,name):
        self._status = "ON"
        self._name = name
        return "Smart light is now on"

    def turn_off(self):
        self._status = "OFF"

    def device_info(self):
        return self._name, self._status

    def set_brightness_level(self,level):

        if 0< level <100:
            print(f"brightness is set to {level} %")



objsl = Smartlight()
print(objsl.turn_on("Bulb"))
print(objsl.device_info())
objsl.turn_off()
objsl.set_brightness_level(10)
print(objsl.device_info())




