create Database DB_Employees;
USE DB_Employees;
create table Employees(
empId int primary key,
empName varchar(20) not null,
salary float(3)
);

create table Device(
DevID int primary key,
Dname varchar(20) not null,
empId int,
Foreign Key (empId) references Employees(empId)
);