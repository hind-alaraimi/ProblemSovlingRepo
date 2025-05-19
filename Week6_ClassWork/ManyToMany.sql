Create Database UniversityDB;
USE UniversityDB;

CREATE TABLE StudentTB(
STU_ID int primary key,
Stu_name varchar(20) not null,
email varchar(30) not null,
Spec varchar(30) not null
);

CREATE TABLE COURSE(
CID int primary key,
Cname varchar(30),
credits int not null
);

CREATE TABLE Enrollment(
SID int,
CID int,
Primary key (SID, CID),
Foreign key (SID) references StudentTB(STU_ID),
Foreign key (CID) references COURSE(CID)
)
