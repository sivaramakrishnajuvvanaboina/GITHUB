# OOPS Concept in Python

class CAR:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def show_car(self):
        print("The car price is:", self.price)
        print("The car brand name is:", self.brand)

class SetParts(CAR):
    def __init__(self,price,brand,wheels):
        self.wheels=wheels
        CAR.__init__(self, price, brand)

    def display(self):
        print("The wheel:",self.wheels)

def main():
    obj = SetParts(900000, "Audi","MRF")
    obj.show_car()
    obj.display()
