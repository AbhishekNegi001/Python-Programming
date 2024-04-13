class Car:
    #constructor
    def __init__(self, brand, price, speed1):
        self.brand = brand
        self.price = price
        self.speed = speed1

car1 = Car("BMW", 2000000, 150)
car2 = Car(1231, 1000000, "huihuihhui")

print("Car 1 :")
print("Name :",car1.brand)
print("Price :",car1.price)
print("Speed :",car1.speed)
print()

print("Car 2 :")
print("Name :",car2.brand)
print("Price :",car2.price)
print("Speed :",car2.speed)
