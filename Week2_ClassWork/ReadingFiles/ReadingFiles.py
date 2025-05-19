File1 = open("file1.txt","r")
line = File1.readline()
while line != "":
    print(line)
    line = File1.readline()

File1.close()

#---------

file2 = open("file2.txt","r")
line2 = file2.readline()
print(float(line2))
print(int(line2))
print(str(line2))
print



