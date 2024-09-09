class shape:

    def print_shape_area(self):
        print("")

class circle(shape):
    def print_shape_area(self):
        print("Area of circle")
        super().print_shape_area()
class rectangle(shape):
    def print_shape_area(self):
        print("Area of rectangle")
        super().print_shape_area()


circle1 = circle()
circle1.print_shape_area()
rectangle1 = rectangle()
rectangle1.print_shape_area()