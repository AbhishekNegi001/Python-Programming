keys = ["apple","mango"]
values = [13, 42]

fruits = dict(zip(keys, values))
print(fruits)

ls1, ls2 = fruits
print(ls1)
print(ls2)

print(fruits.keys())
print(fruits.values())
print(type(fruits.keys()))

dict_keys = fruits.keys()
dict_values = fruits.values()
print(dict_keys)
print(dict_values)
print(type(dict_keys))
