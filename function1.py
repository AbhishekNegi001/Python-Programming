#print even numbers from the list

def func(lst):
    for i in lst:
        if(i%2 is 0):
            print(i)

lst = [12,23,42,4,7]
func(lst)
