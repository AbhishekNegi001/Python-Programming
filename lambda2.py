#sort a list of pair of tuple according to 1st index of tuple

lst = [(12, 54), (6,55), (13,30)]

lst.sort()
print(lst)

#using normal function
def k(x):
    return x[1]

lst.sort(key=k)
print(lst)

#using lamda function
lst.sort(key = lambda x : x[1])
print(lst)
