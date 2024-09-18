# Task 1: Implementing Base Class

class MusicalInstrument:
    def __init__(self, name,type):
        self.__name = name
        self.__type = type
        self.__is_tuned = False

    # getter for name
    @property
    def name(self):
        return self.__name
    # setter for name
    @name.setter
    def name(self,name):
        self.__name = name

    # getter for type
    @property
    def type(self):
        return self.__type
    # setter for type
    @type.setter
    def type(self,type):
        self.__type = type

    def play(self):
        print(f"The {self.__name} is being played")

    def tune(self):
        self.__is_tuned = True
        print(f"The {self.__name} is tuned")

    def check_tuning(self):
        if self.__is_tuned:
            print(f"The current tuning status is '{self.__type}'")
        else:
            print("Their is no tuning")

if __name__ == "__main__":
    instrument = MusicalInstrument("guitar","string")
    instrument.play()
    instrument.tune()
    instrument.check_tuning()
    print(instrument.name)
    instrument.name = "Violin"
    print(instrument.name)



