# Data_Rep_Project 2021

**GMIT Lecturer:** Andrew Beatty
**Student:** Conor O'Riordan G00387832@gmit.ie

This repository contains all of the documentation for my project for the Data Representation module of the GMIT Data Analytics program. The project is a simple organisation management system that could be used by a small company to manage locations, departments and employees.

## Overview of the project

1. The data is stored in a MySQL database.
2. The database queries are defined using the `DAO.py` database access object.
3. The `server.py` application server calls the queries and returns the results as JSON objects.
4. The is a `login` html file that requries a username and password in order to access the main CRUD app.
5. AJAX calls are made in the `index` html file and the results are displayed in nice tables in web browser.


## Database Schema
* The database has four tables.
* One table just for creating users for login in purposes. Table is called *users*
* Three related tables for the main CRUD app
* *locations* table with *locID* as the primary key
* *departments* table with *deptID* as the primary key and *locations* as the foreign key to the *locations* table
* *employees* table with *empID* as the primary key and *dept* as the foreign key to the *departments* table
* The `initdb.sql` provides an overview of the database tables

```
CREATE TABLE locations(
    locID INT NOT NULL AUTO_INCREMENT,
    loc_name VARCHAR(255) DEFAULT NULL,
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
    CONSTRAINT FK_locdept 
    FOREIGN KEY (location)
    REFERENCES locations(locID)
    ON DELETE RESTRICT
    );

CREATE TABLE employees(
    empID INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) DEFAULT NULL,
    title VARCHAR(255) DEFAULT NULL,
    salary INT DEFAULT NULL,
    dept INT DEFAULT NULL,
    PRIMARY KEY (empID),
    CONSTRAINT FK_deptEmp
    FOREIGN KEY (dept)
    REFERENCES departments(deptID)
    ON DELETE RESTRICT
    );
```

## Accessing the project

The best way to access the code for this project is to clone the repository from Github:

```
git clone https://github.com/conor1982/Data_Rep_Project

```

The project is currently hosted live on pythonanywhere and can be viewed and tested by clicking <a href="http://conor1982.pythonanywhere.com/login">here</a>.

Allowable "user : password" combinations are:
* **username**:admin **password**:admin
* **username**:conor **password**:1982
* **username**:andrew **password**:lecturer
* **username**:course **password**:datarep



## Instructions for running the project

1. Clone the repository. `git clone https://github.com/conor1982/Data_Rep_Project`
2. Create a MySQL database called `organisation` with the initdb.sql file.
3. Edit the `dbconfig.py` file adding your MySQL host, database, user and password information.
4. Run `server.py` from your command line locally and access via `http://127.0.0.1:5000/`

**OR**

5. Create a virtual environment, and use `pip` to install the dependancies from the `requirements.txt` file.
6. Set `server.py` as the FLASK_APP and run flask.
7. Using a web browser access `http://127.0.0.1:5000/` (assuming you are using the local host to serve the website)


