class Human:
    #class variable - static variable - belong to class
    population = 0
    data = []

    def __init__(self, name, age):
        #instance variable - belong to instance(object) of class 
        self.name = name
        self.age = age
        Human.population+=1
        Human.data.append(self.name)

    def getter(self):
        print(f"Name : {self.name}, Age : {self.age}, Population : {Human.population}")
        print(f"Data : {Human.data}")

h1 = Human("Abhishek", 21)
h1.getter()

h2 = Human("Anuj", 13)
h2.getter()
