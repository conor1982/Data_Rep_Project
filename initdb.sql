CREATE DATABASE organisation;

USE organisation;

CREATE TABLE locations(
    locID INT NOT NULL AUTO_INCREMENT,
    location VARCHAR(255) DEFAULT NULL,
    type VARCHAR(255) DEFAULT NULL,
    years_occupancy INT DEFAULT NULL,
    PRIMARY KEY (locID)
    );

CREATE TABLE departments(
    deptID INT NOT NULL AUTO_INCREMENT,
    dept_name VARCHAR(255) DEFAULT NULL,
    budget INT DEFAULT NULL,
    location INT DEFAULT NULL,
    PRIMARY KEY (deptID),
    CONSTRAINT FK_locdept FOREIGN KEY (location)
    REFERENCES locations(locID)
    );

CREATE TABLE employees(
    empID INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) DEFAULT NULL,
    salary INT DEFAULT NULL,
    dept INT DEFAULT NULL,
    PRIMARY KEY (empID),
    CONSTRAINT FK_deptEmp
    FOREIGN KEY (dept)
    REFERENCES departments(deptID)
    );

CREATE TABLE users(
   userID INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(255) DEFAULT NULL,
   password varchar(255) DEFAULT NULL,
   PRIMARY KEY (userID)
   );


INSERT INTO locations (location, type, years_occupancy) VALUES ("Killarney (Head Office)", "Owned", 12);
INSERT INTO locations (location, type, years_occupancy) VALUES ("Cork", "Leased", 1);
INSERT INTO locations (location, type, years_occupancy) VALUES ("Belfast", "Leased", 3);
INSERT INTO locations (location, type, years_occupancy) VALUES ("London", "Owned", 8);
INSERT INTO locations (location, type, years_occupancy) VALUES ("New York", "Leased", 2);

INSERT INTO departments (dept_name, budget, location) VALUES ("Sales", 50000, 1);
INSERT INTO departments (dept_name, budget, location) VALUES ("Analytics", 100000, 1);
INSERT INTO departments (dept_name, budget, location) VALUES ("Research", 250000, 1);
INSERT INTO departments (dept_name, budget, location) VALUES ("IT Support", 20000, 2);
INSERT INTO departments (dept_name, budget, location) VALUES ("Logisitcs", 55000, 2);
INSERT INTO departments (dept_name, budget, location) VALUES ("Investment", 1000000, 4);
INSERT INTO departments (dept_name, budget, location) VALUES ("Data Quality", 1000000, 5);
INSERT INTO departments (dept_name, budget, location) VALUES ("Customer Support", 50000, 3);

INSERT INTO employees (name, title, salary,dept) VALUES ("Conor O'Riordan","Head of Analytics",150000, 3);
INSERT INTO employees (name, title, salary,dept) VALUES ("Sean Smith","Data Scientist",100000, 3);
INSERT INTO employees (name, title, salary,dept) VALUES ("Rachel Nolan","Sales Manager",80000, 2);
INSERT INTO employees (name, title, salary,dept) VALUES ("Paul Lyne","Sales Analyst",50000, 2);
INSERT INTO employees (name, title, salary,dept) VALUES ("Tom O'Connor","Sales Analyst",50000, 2);
INSERT INTO employees (name, title, salary,dept) VALUES ("Owen McGuire","Research Lead",100000, 4);
INSERT INTO employees (name, title, salary,dept) VALUES ("William O Donoghue","Research Lead",85000, 4);
INSERT INTO employees (name, title, salary,dept) VALUES ("Alan Donegan","Logistics Manager",750000, 6);
INSERT INTO employees (name, title, salary,dept) VALUES ("Miriam Lucey","Logistics Analyst",500000, 6);
INSERT INTO employees (name, title, salary,dept) VALUES ("Sarah Tracey","Logistics Analyst",500000, 6);
INSERT INTO employees (name, title, salary,dept) VALUES ("Colm Cooper","Head of Investment",100000, 7);
INSERT INTO employees (name, title, salary,dept) VALUES ("Roy Keane","Investment Analyst",800000, 7);
INSERT INTO employees (name, title, salary,dept) VALUES ("Patrick Smith","Head of Data Quality",800000, 8);
INSERT INTO employees (name, title, salary,dept) VALUES ("Dara Moynihan","Data Quality Analyst",800000, 8);
INSERT INTO employees (name, title, salary,dept) VALUES ("Liam Kearney","Customer Success Lead",800000, 9);
INSERT INTO employees (name, title, salary,dept) VALUES ("Patrick O'Sullivan","Customer Success Lead",800000, 9);

INSERT INTO users (name,password) VALUES ("admin","admin");
INSERT INTO users (name,password) VALUES ("conor","1982");
INSERT INTO users (name,password) VALUES ("andrew","lecturer");
INSERT INTO users (name,password) VALUES ("course","datarep");





