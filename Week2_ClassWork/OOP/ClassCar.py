class Car:
    def __init__(self,brand,model,price,year):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        
    def display_model(self):
        return self.model,self.year
        
    def discount(self):
        return self.price-(self.price*0.2)
    
car1 = Car("Toyota","Corolla",4800,2022)
car2 = Car("Nissan","Sentra",3000,2019)

print(car1.display_model()[0],car1.display_model()[1],"price:",car1.discount())
print(car2.display_model()[0],car2.display_model()[1],"price:",car2.discount())
