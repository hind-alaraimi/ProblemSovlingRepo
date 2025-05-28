import pandas as pd

store_sale1 = pd.read_csv('store_sales_1.csv')
store_sale2 = pd.read_csv('store_sales_2.csv')
store_sale3 = pd.read_csv('store_sales_3.csv')

salesDF = pd.concat([store_sale1, store_sale2, store_sale3], ignore_index=True)
print("Combined Shape:", salesDF.shape)
print(salesDF.head())

#Transform:
#Missing values
salesDF['Qty'] = salesDF['Qty'].fillna(salesDF['Qty'].mode()[0]).astype(int)
salesDF['Unit_Price'] = salesDF.groupby('ProductName')['Unit_Price'].transform(
    lambda x: x.fillna(x.median())
)

global_median = salesDF['Unit_Price'].median()
salesDF['Unit_Price'] = salesDF['Unit_Price'].fillna(global_median)

salesDF['CustomerID'] = salesDF['CustomerID'].fillna('Guest')
salesDF['ProductName'] = salesDF['ProductName'].fillna('Unknown Product')
salesDF['SaleDate'] = pd.to_datetime(salesDF['SaleDate'])
salesDF['SaleDate'] = salesDF['SaleDate'].fillna(pd.Timestamp.today())

#Data type:
salesDF['Qty'] = salesDF['Qty'].astype(int)
salesDF['Unit_Price'] = salesDF['Unit_Price'].astype(float)
salesDF['SaleDate'] = pd.to_datetime(salesDF['SaleDate'])

salesDF['StoreName'] = salesDF['StoreID'].astype(str).str.strip().str.upper()
stores_df = salesDF[['StoreName']].drop_duplicates().reset_index(drop=True)
stores_df['StoreID'] = stores_df.index + 1 

#New column:
salesDF['Total_Price'] = salesDF['Qty'] * salesDF['Unit_Price']

#Currency conversion:
# Convert USD to OMR only if currency is 'USD'
usd_mask = salesDF['CurrencyType'].str.upper() == 'USD'
OMR_RATE = 0.38

salesDF.loc[usd_mask, 'Total_Price_OMR'] = salesDF.loc[usd_mask, 'Total_Price'] * OMR_RATE
salesDF.loc[usd_mask, 'CurrencyType'] = 'OMR'

# If other currencies exist, preserve or handle separately
salesDF['Total_Price_OMR'] = salesDF['Total_Price_OMR'].fillna(salesDF['Total_Price'])  # fallback for already-OMR rows

#remove duplicates:
salesDF.drop_duplicates(inplace=True)

#to CSV:
salesDF.to_csv('cleaned_sales_data.csv', index=False)

# Products Table
products_df = salesDF[['ProductName', 'Unit_Price']].drop_duplicates().reset_index(drop=True)
products_df['ProductID'] = products_df.index + 1  # generate PK

# Customers Table
customers_df = salesDF[['CustomerID']].drop_duplicates().reset_index(drop=True)
customers_df['CustomerKey'] = customers_df.index + 1  # generate PK

# Stores Table (if StoreID column exists)
stores_df = salesDF[['StoreName']].drop_duplicates().reset_index(drop=True)
stores_df['StoreKey'] = stores_df.index + 1

# Merge into sales
salesDF = salesDF.merge(stores_df, on='StoreName', how='left')

# Now use StoreKey instead of StoreID in sales_final

# Sales Table (linking foreign keys)
# First, merge ProductID, CustomerKey, etc. into main salesDF
sales_cleaned = salesDF.merge(products_df, on=['ProductName', 'Unit_Price'], how='left')
sales_cleaned = sales_cleaned.merge(customers_df, on='CustomerID', how='left')

sales_final = sales_cleaned[[
    'CustomerKey', 'ProductID', 'StoreKey',
    'Qty', 'SaleDate', 'Total_Price', 'Total_Price_OMR'
]]

#LOAD:
#Load into MySQL server:
import pandas as pd
from sqlalchemy import create_engine
import pymysql  # Just to enable mysql+pymysql connection string

# Create SQLAlchemy engine:
engine = create_engine("mysql+pymysql://root:root@localhost:3306/sales_DB")

# Send cleaned DataFrame to MySQL:
products_df.to_sql('Products', con=engine, if_exists='replace', index=False)
customers_df.to_sql('Customers', con=engine, if_exists='replace', index=False)
stores_df.to_sql('Stores', con=engine, if_exists='replace', index=False)
sales_final.to_sql('Sales', con=engine, if_exists='replace', index=False)


print("Data successfully loaded into MySQL!")