class Car:
    
    #constructor
    def __init__(self, brand, price, speed1):
        self.brand = brand
        self.price = price
        self.speed = speed1

    #class method
    def getter(self):
        print("Name :",self.brand)
        print(f"Price : {self.price}")
        print("Speed : {}".format(self.speed))

car1 = Car("BMW", 2000000, 150)
car2 = Car(1231, 1000000, "huihuihhui")

print("Car 1 :")
car1.getter()
print()

print("Car 2 :")
car2.getter()
