"""
amount = 100
Balance = int(input("Enter balance: "))

if amount > Balance:
    raise ValueError("Amount exceeds balance")
    Balance -= amount
    
print("balance: ",Balance)
    """
#Try and except:
try:
    file1 = open('File.txt','r')
    st = file1.read()
    print(st)

except IOError:
    print("Could not open file")
finally:
    file1.close()
    print("File closed")

    
    
    
    
    
    
    
    