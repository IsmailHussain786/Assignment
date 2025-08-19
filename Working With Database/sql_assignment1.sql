create database Assignment;
use assignment;

create table Customer(
customer_id int,
cust_name varchar(20),
city varchar(20),
grade int,
salesman_id int
);


create table Orders(
ord_no int ,
purch_amt decimal,
ord_date date,
customer_id int ,
salesman_id int
);
alter table orders
modify purch_amt double(6,2);


create table Salesman(
 salesman_id int,
 name varchar(20),
 city varchar(20),
 commission decimal
 );
alter table Salesman
modify commission double(5,2);
 
create table Emp_details(
Emp_id int ,
Emp_firstName varchar(20),
Emp_lastName varchar(20),
Emp_dpt int
);

create table Item_mast(
Prod_id int ,
Prod_name varchar(30),
Prod_price float ,
Prod_com int
);



insert into Customer
values
(3002,"Nick Rimando","New York",100,5001),
(3007,"Brad Davis","New York",200,5001),
(3005,"Graham Zusi","California",200,5002),
(3008,"Julian Green","London",300,5006),
(3009,"Geoff Cameron","Berlin",100,5003),
(3003,"Jozy Altidor","Moscow",200,5007),
(3001,"Brad Guzan","London",NULL,5005);

select * from customer;
insert into orders
values
(70001,150.5,"2012-10-05",3005,5002),
(70009,270.65,"2012-09-10",3001,5005),
(70002 ,65.26,"2012-10-05", 3002, 5001),
(70004 ,110.5,"2012-08-17", 3009, 5003),
(70007 ,948.5,"2012-09-10", 3005, 5002),
(70005 ,2400.6,"2012-07-27", 3007, 5001),
(70008 ,5760,"2012-09-10", 3002, 5001),
(70010 ,1983.43,"2012-10-10", 3004, 5006),
(70003 ,2480.4,"2012-10-10", 3009, 5003),
(70012 ,250.45,"2012-06-27", 3008, 5002),
(70011, 75.29,"2012-08-17", 3003, 500),
(70013 ,3045.6,"2012-04-25", 3002, 500);


select * from orders;

insert into Salesman
values
(5001,"James Hoog","New York",0.15),
(5002,"Nail Knite","Paris",0.13),
(5005,"Pit Alex","London",0.11),
(5006,"Mc Lyon","Paris",0.14),
(5007,"Paul Adam","Rome",0.13),
(5003,"Lauson Hen","San Jose",0.12);

select * from salesman;

insert into emp_details
values
(127323,"Michale ","Robbin",57),
(526689,"Carlos","Snares",63),
(843795,"Enric","Dosio ",57),
(328717,"Jhon","Snares",63),
(444527,"Joseph","Dosni ",47),
(659831,"Zanifer","Emily ",47),
(847674,"Kuleswar","Sitaraman",57),
(748681,"Henrey","Gabriel",47),
(555935,"Alex","Manuel",57),
(539569,"George","Mardy ",27),
(733843,"Mario ","Saule ",63),
(631548,"Alan","Snappy",27),
(839139,"Maria","Foster",57);

select * from emp_details;


insert into item_mast
values
(101,"Motherboard",3200.00 ,15),
(102,"Keyboard ", 450.00 ,16),
(103,"ZIP drive  ",  250.00, 14),
(104,"Speaker ",  550.00, 16),
(105,"Monitor ", 5000.00, 11),
(106,"DVD drive",  900.00, 12),
(107,"CD drive",  800.00, 12),
(108,"Printer ", 2600.00, 13),
(109,"Refill cartridge",  350.00, 13),
(110,"Mouse",  250.00, 12);




select * from customer;
select * from orders;
select * from salesman;
select * from emp_details;
select * from item_mast;


/*1.write a SQL query to find customers who are either from the city 'NewYork' .
or who do not have a grade greater than 100. Return customer_id, cust_name, city, grade, and salesman_id.*/
select * from customer
where city="New York" or not grade>100;

/*2. write a SQL query to find all the customers in ‘New York’ city who have agradevalue
 above 100. Return customer_id, cust_name, city, grade, and salesman_id.*/
select * from customer
where city="New York" AND grade>100;


# 3rd question remainning 


/*4.write a SQL query to calculate the total purchase amount of all orders. Returntotal purchase amount.*/
select 
sum(purch_amt) as Total_Purchase_Amount
from orders;

/*5.write a SQL query to find the highest purchase amount ordered by each customer.
Return customer ID, maximum purchase amount*/
select 
customer_id,
max(purch_amt) as Max_Amt
from orders
group by customer_id
order by Max_Amt desc;

/*write a SQL query to calculate the average product price.
 Return average product price*/
 
 
 
 select 
 avg(Prod_price) as PRODUCT_PRICE
 FROM item_mast;
 
 







