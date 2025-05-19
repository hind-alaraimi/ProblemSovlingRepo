use universityDB;

CREATE TABLE Departments2(
dept_ID int primary key,
deptName varchar(20),
Dept_status varchar(20),
CONSTRAINT deptName_Unq UNIQUE(deptName)
);

CREATE TABLE StudentTB2(
Stu_ID int primary key,
StuName varchar(20),
Age int,
dept_ID int,
Foreign key (dept_ID) references Departments2(dept_ID) ON DELETE CASCADE
);

drop table Departments2;

ALTER TABLE Departments ADD CONSTRAINT Unique (deptName);
insert into StudentTB2 values (1,'Ali',28,12);
insert into Departments2 values (12,'IT','Active');

Drop table StudentTB2;


DELETE FROM StudentTB WHERE STU_ID = 1;
DELETE FROM Departments2 where dept_id = 12;

select * from StudentTB;

INSERT INTO Departments2 VALUES (1, 'IT', 'Active');
INSERT INTO Departments2 VALUES (2, 'HR', 'Active');
INSERT INTO Departments2 VALUES (3, 'Finance', 'Inactive');

INSERT INTO StudentTB2 VALUES (101, 'Alice', 22, 1,'H.@.DF');
INSERT INTO StudentTB2 VALUES (102, 'Bob', 21, 2,'A@.DF');
INSERT INTO StudentTB2 VALUES (103, 'Charlie', 23, 1,'SS.@AD.DF');
INSERT INTO StudentTB2 (Stu_ID,Age) VALUES (107, 23);


Alter table StudentTB2
add email varchar(20) Unique;

ALTER TABLE StudentTB2
MODIFY StuName VARCHAR(20) NOT NULL;

DELETE FROM StudentTB WHERE Stu_ID = 107;

SELECT * FROM StudentTB2

ALTER TABLE StudentTB DROP CONSTRAINT 