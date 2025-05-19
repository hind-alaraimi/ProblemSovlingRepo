Create Database LibraryDB;
USE LibraryDB;

CREATE TABLE Authors(
Author_ID int Primary key,
Author_Name varchar(20) not null,
Age int not null
);

CREATE TABLE Books(
Book_ID int primary key,
Book_Name varchar(30) not null,
Release_Date Date not null,
Author_ID int,
Foreign key (Author_ID) references Authors(Author)
);