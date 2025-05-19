"""
txtfile = open('words.txt','r')
s = ""
for i in txtfile:
    s += i
s = s.replace("\n"," ")
words = s.split(" ")
print(words)
"""
    
#rstrip: remove new line


# Reading Chars:
txtfile = open('words.txt','r')

char = txtfile.read(1)
while char != "":
    char = txtfile.read(1)`
    print(char, end="")
