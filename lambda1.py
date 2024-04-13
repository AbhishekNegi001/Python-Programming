#normal funciotn
def larger1(a,b):
    if a>b :
        return a
    else:
        return b
print(larger1(13,25))

#lambda function
larger2 = lambda a,b : a if a>b else b
print(larger2(13,25))
