import pandas as pd
"""
series = pd.Series([10,20,30],index=['Apple','Banana','Mango'])
print(series)
print()
s = pd.Series({"USA":120,
                "Germany":200,
                "Egypt":1400})
print(s["USA"])
#print(s[0])
"""

"""

sales = pd.Series({
    'Apple': 150,
    'Banana': 200,
    'Orange': 120,
    'Milk': 75,
    'Bread': 90,
    'Cheese': 40,
    'Eggs': 130
})

print(sales.tail())

Dct1 = {'Milk':120,'Bread':80,'Eggs':200,'Cheese':150,'Butter':90}
serGroceries = pd.Series(Dct1)
print()
print(serGroceries)

print(sum(serGroceries))
print((max(serGroceries)))

print(serGroceries[serGroceries == max(serGroceries)])
"""
"""
data = pd.read_csv('sales_data.csv',encoding='ISO-8859-1')
months = pd.Series(data['Sales'].values,index=data['Month'],name="Sales")
print(months)
"""


fruitsData = pd.read_csv('Fruits.csv')
fruit = pd.Series(fruitsData['Price'].values,index=fruitsData['Fruit'])
print(fruit)

print("Mango: ",fruit['Mango'])

fruit['Pineapple'] = 3.5
print(fruit,'\n')

nfruit = fruit+(fruit*0.1)
print("Increasing 10% of price: ")
print(nfruit)

