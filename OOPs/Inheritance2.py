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
        print()

class Employee(Human):
    #reinitiate constructor
    def __init__(self,name, age, post, empid):
        '''
        self.name = name
        self.age = age
        '''
        super().__init__(name, age)
        self.post = post
        self.empid = empid
    def getter(self):
        print(f"Name : {self.name}, Age : {self.age}, Employee Id: {self.empid}, Population : {Human.population}")
        print(f"Data : {Human.data}")
        print()
        
h1 = Human("Abhishek", 21)
h1.getter()

h2 = Human("Anuj", 13)
h2.getter()

emp2 = Employee("Ajay", 34,'SDE', 12345)
emp2.getter()

emp1 = Employee("Rahul", 43)
emp1.getter()
