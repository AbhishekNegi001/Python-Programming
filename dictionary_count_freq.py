txt = "Hello world welcome to python program"
dict_letter = {}
for i in txt:
    if i in dict_letter:
        dict_letter[i] += 1
    else:
        dict_letter[i] = 1
dict_letter.pop(" ")
print(txt)
print(dict_letter)
for key, value in dict_letter.items():
    print(key,value,sep=' : ')
