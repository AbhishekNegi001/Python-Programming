# normal function to add two numbers
print("Normal Function")
def sum1(a, b):
    return a+b
print(sum1)
print(type(sum1))
print(sum1(5,10))
print()

#lambba function
print("Lambda Function")
print( (lambda a,b : a+b)(5,10) )
sum2 = lambda a,b : a+b
print(sum2)
print(type(sum2))
print(sum2(5,10))


