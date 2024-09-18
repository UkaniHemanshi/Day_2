# Task 4: Demonstration Code
# Write a script that does the following:
# 1.Instantiate at least one Guitar, Piano, and Drum object.
# 2.Call the tune() method for each instrument.
# 3.Use the test_instruments(instruments) function to call the methods on all instruments.
# 4.Show how encapsulation works by attempting to access and modify private attributes directly,
# and explain why it's not allowed.

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
        return f"The {self.__name} is being played"

    def tune(self):
        self.__is_tuned = True
        return f"The {self.__name} is tuned"

    def check_tuning(self):
        if self.__is_tuned:
            return f"The current tuning status is '{self.__type}'"
        else:
            return "Their is no tuning"

class Guitar(MusicalInstrument):
    def __init__(self,name,type):
        super().__init__(name,type)

class Piano(MusicalInstrument):
    def __init__(self,name,type):
        super().__init__(name,type)

def test_instruments(instrument_list):
    for instrument in instrument_list:
        print(f"This is play method for {instrument.name} : {instrument.play()}")
        print(f"This is tune method for {instrument.name} : {instrument.tune()}")
        print(f"This is check_tuning method for {instrument.name} : {instrument.check_tuning()}")
        print()

if __name__ == "__main__":
    guitar = Guitar("Guitar","Strumming")
    piano = Piano("Piano","Playing")

    # Call the tune() method for each instrument.
    print("Call the tune() method for each instrument:\n")
    guitar.tune()
    piano.tune()

    # Use the test_instruments(instruments) function to call the methods on all instruments.
    print("\nUse the test_instruments(instruments) function to call the methods on all instruments\n")
    instrument_list = [guitar,piano]
    test_instruments(instrument_list)

    # Show how encapsulation works by attempting to access and modify private attributes directly, and explain
    # why it's not allowed.
    instrument = MusicalInstrument('Guitar','Playing')
    print(instrument.__name) ## this error I have get after using private variable directly
