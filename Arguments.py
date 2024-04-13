# Default arguments
#note: default arguments are always given after the non default arguments
def func1(name, course = "Default"):
    print(f"Name : {name} , Course : {course}")

print("Default arguments")
func1("Abhishek")
func1("Vijay", "BCA")
print()

# Arbitary arguments
# Stores in form of tuple.
# Can take any number of arguments from 0 to N
# format of declaring arbitary arguments : *<variable-name>
def func2(*args):
    print(type(args))
    print(args)

print("Arbitary arguments")
func2()
func2(12)
func2(12,True, "Hello")
print()

#Keyword arguments
# stores the data as a dictionary in form of key value pair
# Can take any number of arguments from 0 to N
# format of declaring keyword arguments : **<variable-name>
def func3(**kwargs):
    print(type(kwargs))
    print(kwargs)

print("Keyword arguments")
func3()
func3(Name="Abhishek")
func3(Name="Abhishek", Age=21)
print()

#Multiple type of arguments
def func4(a, b, c="Default", *args, **kwargs):
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
func4(12, 14)
func4(13, "hello", 14)
func4(345, 12, "wew", 12,13,"er")
func4("string", 12, 23, 3, 2,  13, name = "arjun", age = 13)
