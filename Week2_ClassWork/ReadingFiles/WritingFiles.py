#Write to an empty file:
FileN = open("file.txt",'w')
FileN.write("This is new file")
FileN.close()

#Read the created file:
FileN = open("file.txt",'r')
print(FileN.read())

FileN.close()
