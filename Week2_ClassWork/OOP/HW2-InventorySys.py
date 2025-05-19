

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def getName(self):
        return self.name
    def getQuantity(self):
        return self.quantity
    def getPrice(self):
        return self.price
    

    def updateQuantity(self, newQuantity):
        self.quantity = newQuantity
    
    def updatePrice(self, newPrice):
        self.price = newPrice
    

Inventory = []
print(" Inventory Menu: ")
print(" 1. Add Item \n 2. View all items \n 3.Update item  \n 4. Delete Item \n 5. Search for Item")
flag = True
while flag:
    print("-"*50)
    userChoice = int(input("Enter your Choice: " ))

    if userChoice == 1 :
        name = input("Enter item name: " )
        quantity = int(input("Enter quantity: " ))
        price = float(input("Enter price: " ))
        item1 = Item(name , quantity , price)
        Inventory.append(item1)
        print("Item added sucessfully!" )
    elif userChoice == 2 :
        print(" --- Inventory List --- ")
        print(" Name| Quantity | Price ")
        print("---------------------------")
        for item in Inventory:
            print(item.getName() ,"|" , item.getQuantity() ,"|" , item.getPrice())
            
    elif userChoice == 3 :
        name = input("Enter item name: " )
        for item in Inventory :
            if item.getName() == name :
                userChange = input(" Quantity (Q) or Price (P) ? ")
                if userChange.upper() == "Q" :
                    newQ = int(input("Enter new quantity: " ))
                    item.updateQuantity(newQ)
                    break
                else:
                    newP = int(input("Enter new price: " ))
                    item.updatePrice(newP)
                    break
        
    elif userChoice == 4 :
         name = input("Enter item name: " )
         for item in Inventory :
            if item.getName() == name :
                Inventory.remove(item)
                break
            else:
                print("There is no item like this" )
        
    elif userChoice == 5 :
        name = input("Enter item name: " )
        for item in Inventory :
            if item.getName() == name :
                print(" Item name was found ")
                print(item.getName() ,"|" , item.getQuantity() ,"|" , item.getPrice())
                break
            else:
                print(" Item name was not found ")
    elif userChoice == 6:
        flag = False
    else:
        print("Error: There is no number option like this. Try Again. ") 
         
                
  