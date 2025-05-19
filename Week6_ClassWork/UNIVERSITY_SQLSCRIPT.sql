create database universityDB;
use universityDB;

CREATE TABLE STUDENT2(
St_ID numeric(6) primary key check(St_ID>0),
St_Major Varchar(30),
St_Cohort numeric(4) not null
);

create table employee(
Em_ID numeric(6) primary key check(Em_ID>0),
Em_Office varchar(4) not null,
Em_Ext numeric(4) check(Em_Ext>1000)
);

create table COLLEGE(
Cl_Code varchar(3) primary KEY,
Cl_Name varchar(40) not null,
Cl_Dean varchar(30)
);

create table DEPARTMENT(
Dp_Code varchar(4) primary KEY,
Dp_Name varchar(40) not null,
Dp_HoD varchar(30),
Dp_Col VARCHAR(3),
FOREIGN KEY (Dp_Col) references COLLEGE(Cl_Code)
);


create table BORROWER(
Br_ID numeric(6) primary KEY Check(Br_ID>0),
Br_Name varchar(30) not null,
Br_Dept varchar(4),
Br_Mobile VARCHAR(8) Check(Br_Mobile>90000000) ,
Br_City varchar(20),
Br_House varchar(4),
Br_Type varchar(1) CHECK (Br_Type IN ('S', 'E')),
FOREIGN KEY (Br_Dept) REFERENCES DEPARTMENT(Dp_Code)
);	

create table BOOK(
Bk_ID numeric(6) primary KEY Check(Bk_ID>0),
Bk_Title varchar(50) not null,
Bk_Edition numeric(2),
Bk_ofPages numeric(4) Check(Bk_ofPages>0) ,
Bk_TotalCopies numeric(5),
Bk_RemCopies numeric(5)
);	

create table BOOKTOPIC(
Tp_BkID numeric(6),
Tp_Desc varchar(30) not null,
FOREIGN KEY  (Tp_BkID) REFERENCES BOOK(Bk_ID)
);	

create table COURSES(
Cr_Code VARCHAR(8) primary KEY,
Cr_Title varchar(40) not null,
Cr_CH numeric(2) CHECK(Cr_CH>0),
Cr_ofSec numeric(2) Check(Cr_ofSec>0) ,
Cr_Dept varchar(4),
FOREIGN KEY (Cr_Dept) REFERENCES DEPARTMENT(Dp_Code)
);	

create table LINK(
Li_CrCode varchar(8),
Li_BkID NUMERIC(6),
FOREIGN KEY (Li_CrCode) REFERENCES COURSES(Cr_Code),
FOREIGN KEY (Li_BkID) REFERENCES BOOK(BK_ID),
Li_usage varchar(1) CHECK (Li_usage IN ('T', 'R'))
);

create table REGISTRATION(
Re_BrID NUMERIC(6),
Re_CrCode VARCHAR(8),
FOREIGN KEY (Re_BrID) REFERENCES BORROWER(Br_ID),
FOREIGN KEY (Re_CrCode) REFERENCES COURSES(Cr_Code),
Re_Semester varchar(6) NOT NULL
);


create table ISSUING(
is_BrID NUMERIC(6),
is_BkID NUMERIC(6),
FOREIGN KEY (is_BrID) REFERENCES BORROWER(Br_ID),
FOREIGN KEY (is_BkID) REFERENCES BOOK(BK_ID),
is_DateTaken DATE NOT NULL ,
is_DateReturn DATE,
CHECK (is_DateReturn >= is_DateTaken)
);


INSERT INTO college VALUES('COM', 'Economy', 'Prof. Fahim');

INSERT INTO college VALUES('SCI', 'Science', 'Prof. Salma');

INSERT INTO college VALUES('EDU', 'Education', 'Dr. Hamad');

INSERT INTO college VALUES('ART', 'Arts', 'Dr. Abdullah');

SELECT * FROM COLLEGE;

INSERT INTO department VALUES('INFS','Information Systems','Dr. Kamla','COM');

INSERT INTO department VALUES('FINA','Finance','Dr. Salim','COM');

INSERT INTO department VALUES('COMP','Computer Science','Dr. Zuhoor','SCI');

INSERT INTO department VALUES('BIOL','Biology','Dr. Othman','SCI');

INSERT INTO department VALUES('HIST','History','Dr. Said','EDU');

INSERT INTO department VALUES('CHEM', 'Chemistry', 'Dr. Alaa', 'SCI');

INSERT INTO department (DP_CODE,DP_NAME) VALUES('ITDB', 'Database');
delete from departments where DP_Code = 'ITDB';

CREATE TABLE SUB_DEPT(
DID VARCHAR(4),
DNAME VARCHAR(40) NOT NULL
);

INSERT INTO SUB_DEPT SELECT DP_CODE,DP_NAME FROM DEPARTMENT;

SELECT * FROM DEPARTMENT;
SELECT * FROM SUB_DEPT;

UPDATE DEPARTMENT SET Dp_HoD = 'Dr. Wardah' where Dp_Code = 'ITDB';

INSERT INTO borrower VALUES (92120,'Ali','INFS',99221133,'Seeb','231','S');

INSERT INTO borrower VALUES (10021,'Said','INFS',91212129,'Seeb','100','S');

INSERT INTO borrower VALUES (10023,'Muna','FINA', NULL, 'Barka','12','S');

INSERT INTO borrower VALUES (3000,'Mohammed','COMP',90000009,'Seeb','777','E');

INSERT INTO borrower VALUES (4000,'Nasser','INFS',99100199,'Sur','11','E');

select * from borrower;
update borrower set Br_mobile = 91231992 where Br_ID = 10023;

INSERT INTO student VALUES(92120,'INFS',2012);

INSERT INTO student VALUES(10021,'INFS',2015);

INSERT INTO student VALUES(10023,'FINA',2015);



INSERT INTO employee VALUES(3000,'12',2221);

INSERT INTO employee VALUES(4000,'15',1401);



INSERT INTO book VALUES(1001,'Database1',2,450,150,65);

INSERT INTO book VALUES(1002,'Database2',3,300,100,100);

INSERT INTO book VALUES(2001,'Intro. to Finanace',1,300,75,40);

INSERT INTO book VALUES(3001,'Basic Op Mgmt',1,320,100,77);

INSERT INTO book VALUES(3002,'Chemistry Book',2,500,100,80);

INSERT INTO book VALUES(4001,'Biology',1,345,100,100);

INSERT INTO book VALUES(3003,'Management I',2,560,44,34);

INSERT INTO book VALUES(1003,'Java Prog.',3,555,50,50);



INSERT INTO bookTopic VALUES (1001,'Basic DB Skills');

INSERT INTO bookTopic VALUES (1001,'ERD');

INSERT INTO bookTopic VALUES (1001,'EERD');

INSERT INTO bookTopic VALUES (1002,'SQL');

INSERT INTO bookTopic VALUES (1002,'Pl/SQL');

INSERT INTO bookTopic VALUES (3001,'Management Skills');

select * from bookTopic;

INSERT INTO courses VALUES('COMP4201', 'Database1', 3, 1,'COMP');

INSERT INTO courses VALUES('COMP4202', 'Database2', 3, 2,'COMP');

INSERT INTO courses VALUES('BIOL1000', 'Intro. To Biology', 3, 5,'BIOL');

INSERT INTO courses VALUES('CHEM2000', 'Advanced Chemistry', 2, 2,'CHEM');



INSERT INTO LINK VALUES('COMP4201',1001,'T');

INSERT INTO LINK VALUES('COMP4201',1002,'R');

INSERT INTO LINK VALUES('COMP4202',1002,'T');

INSERT INTO LINK VALUES('BIOL1000',4001,'T');

INSERT INTO LINK VALUES('CHEM2000',3002,'R');



INSERT INTO REGISTRATION VALUES(92120,'COMP4201','FL2015');

INSERT INTO REGISTRATION VALUES(10021,'COMP4202','FL2015');

INSERT INTO REGISTRATION VALUES(92120,'BIOL1000','FL2015');

INSERT INTO REGISTRATION VALUES(92120,'COMP4202','FL2016');

INSERT INTO REGISTRATION VALUES(10021,'CHEM2000','FL2016');



INSERT INTO ISSUING VALUES (92120, 1001, '2015-09-01', '2015-10-30');

INSERT INTO ISSUING VALUES (10021, 1002, '2016-10-30', NULL);

INSERT INTO ISSUING VALUES (92120, 1002, '2015-02-21', '2016-01-01');

INSERT INTO ISSUING VALUES (92120, 3002, '2016-03-30', NULL);

INSERT INTO ISSUING VALUES (10021, 3002, '2014-12-01', NULL);

select * from department;


set @dept_name = 'ITDB' ;
SELECT * FROM Department where Dp_Code = @dept_name;

alter table employee add salary decimal(6,2);

select * from employee;


update employee set salary = salary + (salary*0.2) where em_id > 0;


INSERT INTO book VALUES(1002,'Database2',3,300,100,100);
select * from book;
update book set bk_Edition = 5,Bk_totalCopies = 110 where Bk_ID = 1001;

Delete from book where bk_id = 1002;

select * from student;

Delete from student where st_id = 10021;


select  Bk_title as "book title" from book ;

select salary+(Salary*0.2) from employee;

select distinct Tp_BkID from bookTopic;