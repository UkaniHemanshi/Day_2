# Task 2: Implementing Inheritance

class MusicalInstrument:
    __map = ""
    def __init__(self,name,type):
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

class Guitar(MusicalInstrument):
    def __init__(self,name,number_of_strings):
        super().__init__(name, type= "String")
        self.number_of_strings = number_of_strings

    # Override  play function
    def play(self):
        print(f"The {self.name} is strumming")

class Piano(MusicalInstrument):
    def __init__(self,name,number_of_keys):
        super().__init__(name, type= "Percussion")
        self.number_of_keys  = number_of_keys

    # Override  play function
    def play(self):
        print(f"The {self.name} is playing")

class Drum(MusicalInstrument):
    def __init__(self,name,drum_size):
        super().__init__(name, type= "Wind")
        self.drum_size   = drum_size

    # Override  play function
    def play(self):
        print(f"The {self.name} is playing")

if __name__ == "__main__":
    guitar1 = Guitar("Guitar",5)
    guitar1.play()
    guitar1.tune()
    guitar1.check_tuning()
    guitar1.name = 'Guitar_1'
    guitar1.play()
    print()

    piano1 = Piano("Piano",5)
    piano1.play()
    piano1.tune()
    piano1.check_tuning()
    piano1.name = 'Piano_1'
    piano1.play()
    print()

    drum1 = Drum("Drum","Small")
    drum1.play()
    drum1.tune()
    drum1.check_tuning()
    drum1.name = 'Drum_1'
    drum1.drum_size = "Medium"
    print(drum1.drum_size)
