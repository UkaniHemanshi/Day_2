# Task 3: Polymorphism

class MusicalInstrument:
    def __init__(self, name,type):
        self.name = name
        self.type = type
        self.is_tune = False

    def play(self):
        return f"The {self.name} is {self.type}"
    def check_tuning(self):
        self.is_tune = True
        return f"The {self.name} is tunning !!"

class Guitar(MusicalInstrument):
    def __init__(self,name,type):
        super().__init__(name,type)

class Piano(MusicalInstrument):
    def __init__(self,name,type):
        super().__init__(name,type)

class Violin(MusicalInstrument):
    def __init__(self,name,type):
        super().__init__(name,type)

def test_instruments(instrument_list):
    for instrument in instrument_list:
        print(instrument.play())
        print(instrument.check_tuning())

if __name__ == "__main__":
    guitar = Guitar("Guitar","Strumming")
    piano = Piano("Piano","Playing")
    violin = Violin("Violin","beaten")

    instrument_list = [guitar,piano,violin]
    test_instruments(instrument_list)
