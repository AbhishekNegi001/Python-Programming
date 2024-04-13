import json # importing json module

#json object
x = '{"name" : "Abhishek", "age" : 21 }'
print(x)
print(type(x))
print()

y = json.loads(x)#converting json object into python object as dictionary
print("name :", y["name"])
print(y)
print(type(y))
print()

z = json.dumps(y)#converting from python object(dictionary) to json object
print(z)
print(type(z))