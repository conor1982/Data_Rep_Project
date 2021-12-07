#Database Acccess Object DAO
# Interface between sql db and flask server


#import modules
import mysql.connector
import dbconfig as cfg



#Make DAO Class 
class OrgDAO:


    #db connection
    def ConnectionToDB(self):
        db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['username'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database'],
            pool_name = 'connection_pool',
            pool_size=5
        )
        return db

    # Get a connection from the pool
    def getConnection(self):
        db = mysql.connector.connect(
        pool_name='connection_pool'
        )
        return db

    # Initialise DB connection pool
    def __init__(self):
        db = self.ConnectionToDB()
        db.close()

      #Create Functions (insert into) for location, department and employees

      #create location
    def createLocation(self,location):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into locations (loc_name, type, years_occupancy) values (%s,%s,%s)"
        values = [            
            location["loc_name"],
            location['type'],
            location['years_occupancy']
              ]
        cursor.execute(sql, values)
        db.commit()
        lastRowId = cursor.lastrowid
        db.close()
        return lastRowId
        #return location['location']

    #create department
    def createDepartment(self,dept):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into departments (dept_name, budget, location) values (%s,%s,%s)"
        values = [
            dept['dept_name'],
            dept['budget'],
            dept['location']
            ]
        cursor.execute(sql, values)
        db.commit()
        lastRowId = cursor.lastrowid
        db.close()
        return lastRowId

    #create department
    def createEmployee(self,emp):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into employees (name, title, salary,dept) values (%s,%s,%s,%s)"
        values = [
            emp['name'],
            emp['title'],
            emp['salary'],
            emp['dept']
            ]
        cursor.execute(sql, values)
        db.commit()
        lastRowId = cursor.lastrowid
        db.close()
        return lastRowId

    #Create Functions (select all) for location, department and employees

    #getall locations
    def getAllLocs(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from locations"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertLocToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

     #getall locations
    def getAllDepts(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from departments"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertDeptToDict(result)
            returnArray.append(resultAsDict)
        db.close()

        return returnArray

    #getall employees
    def getAllEmps(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from employees"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertEmpToDict(result)
            returnArray.append(resultAsDict)
        db.close()

        return returnArray

    #Return Data basd on primaryKey ID

    #locations
    def findLocById(self, locID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from locations where locID = %s'
        values = [locID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        loc = self.convertLocToDict(result)
        db.close()
        return loc

    #deparmtents
    def findDeptById(self, deptID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from departments where deptID = %s'
        values = [deptID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        dep = self.convertDeptToDict(result)
        db.close()
        return dep
     

    #employees
    def findEmpById(self, empID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from employees where empID = %s'
        values = [empID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        emp = self.convertEmpToDict(result)
        db.close()
        return emp  

    # Return info on all depts associated with a given location locID
    def getAllDeptByLoc(self, locID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from departments where location = %s;'
        values = [locID]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        
        for result in results:
            resultAsDict = self.convertDeptToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

    # Return info on all employees associated with a given department deptID
    def getAllEmpByDept(self, deptID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select dept from employees where dept = %s;'
        values = [deptID]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        
        returnArray = []
        #for i in results:
        #    returnArray.append(i[0])
        
        for result in results:
            resultAsDict = self.convertEmpToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

    #Update DB Functions

    # update locations
    def updateLoc(self, loc):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "update locations set loc_name = %s, type = %s, years_occupancy = %s where locID = %s"
        values = [
            loc['loc_name'],
            loc['type'],
            loc['years_occupancy'],
            loc['locID']
            ]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return loc

    # update departments
    def updateDept(self, dept):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "update departments set dept_name = %s, budget = %s, location = %s where deptID = %s"
        values = [
            dept['dept_name'],
            dept['budget'],
            dept['location'],
            dept['deptID']
            ]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return dept

    # update employees
    def updateEmp(self, emp):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "update employees set name = %s, title = %s, salary = %s, dept = %s where empID = %s"
        values = [
            emp['name'],
            emp['title'],
            emp['salary'],
            emp['dept'],
            emp['empID']
            ]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return emp

    # Delete Functions

    #delete location based on locID
    def deleteLoc(self, locID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'delete from locations where locID = %s'
        values = [locID]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return {}
        
    #delete department based on deptID
    def deleteDept(self, deptID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'delete from departments where deptID = %s'
        values = [deptID]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return {}
        
    #delete employee based on empID
    def deleteEmp(self, empID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'delete from employees where empID = %s'
        values = [empID]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return {}
    
    #For Login and Users
    # Create user, returns userID of new user
    def createUser(self, user):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into users (name, password) values (%s,%s)"
        values = [
            user['name'],
            user['password'],

        ]
        cursor.execute(sql, values)
        db.commit()
        lastRowId = cursor.lastrowid
        db.close()
        return lastRowId

# Return info on all users
    def getAllUser(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from users'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []

        for result in results:
            resultAsDict = self.convertUserToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

# Return info on user by userID
    def findUserByID(self, userID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from users where userID = %s'
        values = [userID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        user = self.convertUserToDict(result)
        db.close()
        return user

# Update user info for given userID, returns updated info
    def updateUser(self, user):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "update users set name = %s, password = %s where userID = %s"
        values = [
            user['name'],
            user['password'],
            user['userID']
        ]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return user

    # Delete user for given userID, returns empty dictionary/JSON
    def deleteUser(self, userID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'delete from users where userID = %s'
        values = [userID]
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return {}

    #Locations to Dict
    def convertLocToDict(self,result):
        colnames = ['locID','loc_name', 'type', 'years_occupancy']
        loc = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                loc[colName] = value
        return loc

    #departments to dict
    def convertDeptToDict(self,result):
        colnames = ['deptID','dept_name', 'budget', 'location']
        dept = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                dept[colName] = value
        return dept

    #employess to dict
    def convertEmpToDict(self,result):
        colnames = ['empID','name', 'title', 'salary','dept']
        emp = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                emp[colName] = value
        return emp

    # Function to convert user into Dictionary/JSON
    def convertUserToDict(self, result):
        colnames = ['userID', 'name', 'password']
        u = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                u[colName] = value
        return u

# Return info on all employees associated with a given department deptID
    def getAllEmpInDept(self, deptID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select dept from employees where dept = %s;'
        values = [deptID]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        
        returnArray = []
        for i in results:
            returnArray.append(i[0])
        
        #for result in results:
        #    resultAsDict = self.convertEmpToDict(result)
        #    returnArray.append(resultAsDict)
        db.close()
        return returnArray

# Return info on all depts associated with a given location locID
    def getAllLocInDept(self, locID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select location from departments where location = %s;'
        values = [locID]
        cursor.execute(sql, values)
        results = cursor.fetchall()
        
        returnArray = []
        for i in results:
            returnArray.append(i[0])
        
        #for result in results:
        #    resultAsDict = self.convertEmpToDict(result)
        #    returnArray.append(resultAsDict)
        db.close()
        return returnArray           

orgDao = OrgDAO()



