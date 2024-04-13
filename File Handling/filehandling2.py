#uisng with open we don't need to explicity close the file
#it automatically closes itself after the operation


#creates file if doesn't exist, overwrites data
with open("text1.txt",'w') as f: 
    f.write("Hey there \nWelcome to file handling")

#print(f.closed())

#file read
with open("text1.txt","r") as f:
    print(f.read())

print()

#created file if doesn't exit else append the existing data
with open("text1.txt",'a') as f:
    f.write("new statement appended")


with open("text1.txt","r") as f:
    for i in f:
        print(i, end='')

print()
print()

#data overwritten
with open("text1.txt",'w') as f:
    f.write("data overwritten")

with open("text1.txt","r") as f:
    txt = f.readline()
    while(txt!=''):
        print(txt,end='')
        txt = f.readline()
print()
