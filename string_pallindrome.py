txt = "hello"

print(txt)
print(txt[::-1])

if(txt== txt[::-1]):
    print(f"txt is pallindrome")
else:
    print("{} is not pallindrome".format(txt))

