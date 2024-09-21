class Fooditem:
    name = ""
    price = 0.0
    category = ""
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        return f"Name of the food: {self.name}\nPrice of the food: {self.price}\nCategory: {self.category}\n"

class Customer:
    def __init__(self,name,customer_id):
        self.name = name
        self.customer_id = customer_id
        self.order_history = []

    def placeorder(self, fooditem, quantity):
        total_cost = fooditem.price * quantity
        self.order_history.append((fooditem, quantity, total_cost))
        return total_cost

    def view_order_history(self):
        print(f"Order history for {self.name}:")
        for order in self.order_history:
            fooditem, quantity, total = order
            print(f"{quantity}x {fooditem.name} - Total: {total}")

class Regularcustomer(Customer):
    def __init__(self,name,customer_id,r_discount):
        super().__init__(name,customer_id)
        self.r_discount = r_discount

    def placeorder(self, fooditem, quantity):
        total_cost = super().placeorder(fooditem, quantity)
        discounted_total = total_cost * (1 - self.r_discount / 100)
        print(f"Regular Customer {self.name} ordered {quantity}x {fooditem.name} - Total after discount: {discounted_total}")


class Premiumcustomer(Customer):
    p_discount = 0.0
    priority_delivery = False

    def __init__(self,name,customer_id,p_discount,priority_delivery):











































































































































        
        super().__init__(name,customer_id)
        self.p_discount = p_discount
        self.priority_delivery = priority_delivery

    def placeorder(self, fooditem, quantity):
        total_cost = super().placeorder(fooditem, quantity)
        discounted_total = total_cost * (1 - self.p_discount / 100)
        print(f"Premium Customer {self.name} ordered {quantity}x {fooditem.name} - Total after discount: {discounted_total} - Priority Delivery: {self.priority_delivery}")

class Restaurant:
    def __init__(self):
        self.menu = []
        self.customer = []

    def add_food_item(self,food_item):
        self.menu.append(food_item)

    def add_customer(self,customer):
        self.customer.append(customer)

    def display_menu(self):
        print("All food items available in the menu: ")
        for item in self.menu:
            print(item.display_info())

    def display_customer(self):
        print("All customers registered in the restaurant:")
        for customer in self.customer:
            print(customer.name)

def main():

    # create a few instances of fooditem
    food_items = [
        Fooditem("Kaju katli",20,"Desert"),
        Fooditem("Tea",10,"Starter"),
        Fooditem("Sandwich",50,"Main Course")
    ]

    # create display food item
    for item in food_items:
        print(item.display_info())

    # create instances of regularcustomer and premium customer
    customers = [
        Regularcustomer("Dhruv","101",5),
        Regularcustomer("Sachin", "102", 5),
        Regularcustomer("Hemanshi", "103", 5),
        Premiumcustomer("P1","P01",15,True),
        Premiumcustomer("P2","P02",15,True),
    ]

    # add food item and customers
    restaurant = Restaurant()
    for item in food_items:
        restaurant.add_food_item(item)

    for customer in customers:
        restaurant.add_customer(customer)

    # restaurant displaymenu and display customer
    restaurant.display_menu()
    restaurant.display_customer()

    # placing order
    customers[0].placeorder(food_items[0],2)
    customers[4].placeorder(food_items[2],4)

    # View order history for customers
    customers[0].view_order_history()
    customers[3].view_order_history()

if __name__ == "__main__":
    main()