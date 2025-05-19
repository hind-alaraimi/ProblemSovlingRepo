"""
guestType = input("Enter Type of guest: ")
numberOfNights = int(input("Enter Number of Nights: "))
price = 30
if(guestType == "student"):
    totalPrice = (price - (price*0.2)) * numberOfNights
elif(guestType == "regular" and numberOfNights>3):
    totalPrice = (price - (price*0.15)) * numberOfNights
    
else:
    totalPrice = price * numberOfNights
    
print("Total Price: ",totalPrice)
"""


levelOfEarthquake = float(input("Enter calue of earthquack: "))
if (levelOfEarthquake >= 8):
    print("Most structures fall")
elif (levelOfEarthquake >= 7):
    print("Many buildings destroyed")
elif (levelOfEarthquake >= 6):
    print("Many buildings considerably damaged, some collapse")
else:
    print("Damage to poorly construced buildings")

