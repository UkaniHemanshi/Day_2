class car:

    #class attribute
    number_of_cars = 4

    def __init__(self, make1, model1):

        self.make = make1
        self.model = model1
        car.number_of_cars +=1

    # Class method to access class attributes
    @classmethod
    def get_number_of_cars(cls):
         print(f"total cars: {cls.number_of_cars}")


if __name__ == '__main__':

    car1 = car("gtr", "nissan")

    car1.get_number_of_cars()
