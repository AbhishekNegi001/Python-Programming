#creates file if doesn't exist, overwrites data
f = open("text1.txt",'w')
f.write("Hey there \nWelcome to file handling")
f.close()
#print(f.closed())

#file read
f = open("text1.txt","r")
print(f.read())
f.close()
print()

#created file if doesn't exit else append the existing data
f = open("text1.txt",'a')
f.write("new statement appended")
f.close()

f = open("text1.txt","r")
for i in f:
    print(i, end='')
f.close()
print()
print()

#data overwritten
f = open("text1.txt",'w')
f.write("data overwritten")
f.close()

f = open("text1.txt","r")
txt = f.readline()
while(txt!=''):
    print(txt,end='')
    txt = f.readline()
f.close()
print()
