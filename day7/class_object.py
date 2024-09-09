class car:
    wheels = 4
    make = ""
    model = ""
    year = ""

    def display_info(self):
        print(f"car information : \nyear of manufacturing{self.year} \nmake: {self.make}")
if __name__ == '__main__':
    car1 =  car()
    car1.model = "Toyota"
    car1.make = "corolla"
    car1.year = 2020

    car2 = car()
    car2.model = "Honda"
    car2.make = "NSX"
    car2.year = 1996

    car1.display_info()
    car2.display_info()