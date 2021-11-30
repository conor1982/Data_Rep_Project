from DAO import orgDao

#print('ok')

# locations for test
loc1 = {'location': 'kerry',
        'type': 'Leased',
        'years_occupancy':4,
        'locID':7
}

loc2 = {'location': 'galway',
        'type': 'Owned',
        'years_occupancy':1
}

loc3 = {'locID':7,
        'location': 'Sneem',
        'type': 'Leased',
        'years_occupancy':3
}
# departments for test
dept1 = {'dept_name': 'Sales',
        'budget': 150000,
        'location':1
}

dept1 = {'dept_name': 'IT',
        'budget': 50000,
        'location':2
}

dept3 = {'dept_name': 'After Sales Support',
        'budget': 25000,
        'dept_ID':10,
        'location':3
}
#employees for test
emp1 = {'name': 'Eileen',
        'title': 'Sales Analyst',
        'salary':50000,
        'dept':2
}

emp2 = {'name': 'Peadar',
        'title': 'Investment Guru',
        'salary':500000,
        'dept':7
}

emp3 = {'empID':18,
        'name': 'Peadar Lucey',
        'title': 'Investment Strategy',
        'salary':10000,
        'dept':3
}

#user test
user1 = {
        'name':'aideen',
        'password':'conor'
}

user2 = {'userID':'5',
        'name':'leo',
        'password':'connie'
}

# Insert Into Test
#returnValue = orgDao.createLocation(loc1)
#print(returnValue)
#returnValue = orgDao.createLocation(loc2)
#print(returnValue)
#returnValue = orgDao.createDepartment(dept1)
#print(returnValue)
#returnValue = orgDao.createDepartment(dept1)
#print(returnValue)
#returnValue = orgDao.createEmployee(emp1)
#print(returnValue)
#returnValue = orgDao.createEmployee(emp2)
#print(returnValue)

# Get all table contents
#print(" ")
#returnValue = orgDao.getAllDepts()
#print(returnValue)
#print("")
#returnValue = orgDao.getAllEmps()
#print(returnValue)

# contents by ID
#returnValue = orgDao.findLocById(2)
#print("find Loc By Id")
#print(returnValue)
#print("")
#returnValue = orgDao.findDeptById(8)
#print("find Dept By Id")
#print(returnValue)
#print("")
#returnValue = orgDao.findEmpById(12)
#print("find Emp By Id")
#print(returnValue)

# depts by location ID
#returnValue = orgDao.getAllDeptByLoc(4)
#print("Depts by Location")
#print(returnValue)
#print("")

#employess by dept id
#returnValue = orgDao.getAllEmpByDept(9)
#print("find Dept By Id")
#print(returnValue)

#returnValue = orgDao.updateLoc(loc3)
#print(returnValue)
#print("")
#returnValue = orgDao.updateDept(dept3)
#print(returnValue)
#print("")
#returnValue = orgDao.updateEmp(emp3)
#print(returnValue)

#returnValue = orgDao.deleteLoc(1)
#returnValue = orgDao.deleteLoc(8)

#returnValue = orgDao.deleteDept(9)
#returnValue = orgDao.deleteDept(8)

#test user login
#returnValue = orgDao.getAllUser()
#print(returnValue)
#print("")
#print('user id')
#returnValue = orgDao.findUserByID(1)
#print(returnValue)
#print("")
#print('new user')
#returnValue = orgDao.createUser(user1)
#print(returnValue)
#update user
#returnValue = orgDao.updateUser(user2)
#print(returnValue)

#print('delete users')
#returnValue = orgDao.deleteUser(5)


