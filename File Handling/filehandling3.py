#read(): reads whole data
#read(l): reads data of length l
#tell(): tells you about the position of file handle
#seek(): helps to reposition our file handle
#readlines(): read data line by line

with open("text1.txt",'w') as f: 
    f.write("Hey there \nWelcome to file handling")

#print(f.closed())

#file read
with open("text1.txt","r") as f:
    print("position of file handler:",f.tell())
    print("f.read(5) :",f.read(5))#read data upto length of 5
    print("position of file handler:",f.tell())
    
    print("f.read(10) :",f.read(10))#read next data upto length of 10
    print("position of file handler:",f.tell())

    f.seek(3)
    print("position of file handler after reassigning counter:",f.tell())
    print("f.read(10) :",f.read(10))
    print("position of file handler:",f.tell())
    
print()

