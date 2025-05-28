SELECT * FROM salesdb.stores;

-- Make ProductID the primary key of Product
ALTER TABLE Products
ADD PRIMARY KEY (ProductID);

-- Make CustomerID the primary key of Customer
ALTER TABLE Customers 
MODIFY CustomerID VARCHAR(100);

-- Now you can safely add the primary key
ALTER TABLE Customers
ADD PRIMARY KEY (CustomerKEY);

-- Make StoreID the primary key of Store

ALTER TABLE Stores 
MODIFY StoreID VARCHAR(100);

ALTER TABLE Stores
ADD PRIMARY KEY (StoreKey);

SELECT StoreID, COUNT(*) 
FROM Stores
GROUP BY StoreID
HAVING COUNT(*) > 1;

-- Make SaleID the primary key of Sale
ALTER TABLE Sales
ADD PRIMARY KEY (SaleID);

select * from sales;

ALTER TABLE Sales ADD PRIMARY KEY (SaleID);


ALTER TABLE Sales
ADD CONSTRAINT fk_product FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
ADD CONSTRAINT fk_customer FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
ADD CONSTRAINT fk_store FOREIGN KEY (StoreID) REFERENCES Stores(StoreID);



SHOW TABLES;
DESCRIBE Products;
DESCRIBE Customers;
DESCRIBE Stores;
DESCRIBE Sales;

ALTER TABLE Sales
ADD CONSTRAINT fk_sale_product FOREIGN KEY (ProductID)
    REFERENCES Products(ProductID)
    ON DELETE RESTRICT ON UPDATE CASCADE,

ADD CONSTRAINT fk_sale_customer FOREIGN KEY (CustomerKEY)
    REFERENCES Customers(CustomerKEY)
    ON DELETE RESTRICT ON UPDATE CASCADE,

ADD CONSTRAINT fk_sale_store FOREIGN KEY (StoreKey)
    REFERENCES Stores(StoreKey)
    ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE Sales
MODIFY COLUMN storekey INT;

select * from sales;
DESCRIBE Sales;
SELECT * FROM STORES;
drop table CUSTOMERS;

ALTER TABLE STORES MODIFY COLUMN storekey INT;