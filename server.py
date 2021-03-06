from flask import Flask, url_for, request, redirect, abort, jsonify, render_template, abort, session
from DAO import orgDao
#import mysql.connector


#app = Flask(__name__, static_url_path='', static_folder='staticpages')
app = Flask(__name__)
app.secret_key = 'matilda'


# route to index
@app.route('/')
def index():
    if not 'username' in session:
        return redirect(url_for('login'))

    return render_template('index.html',title='Index',name = session['username'])

###########################################################
# Login
# Code adapted from https://pythonbasics.org/flask-http-methods/
# curl http://127.0.0.1:5000/login
@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        submittedName = request.form['name']
        submittedPassword = request.form['password']

       # Get users from database
        foundUsers = orgDao.getAllUser()
        for i in range(len(foundUsers)):
            # compare user name
            if submittedName.lower() == foundUsers[i]["name"].lower():
                app.logger.info('User found')
            # compare user password
                if submittedPassword == foundUsers[i]["password"]:
                    # username and associated password match found
                    app.logger.info('Password matched for user %s', submittedName)
                    session['username'] = submittedName
                    return redirect(url_for('index',name = session['username']))
                else:
                    app.logger.info('Password does not match for user')
                    return render_template('login.html', title='Login', userMessage='Incorrect password entered! Please try again')

      # Otherwise
        app.logger.info('User not found')
        return render_template('login.html', title='Login', userMessage='WARNING: User not found! Please try again')

    else:
        # for GET method
        app.logger.info('Redirect to login')
        return render_template('login.html', title='Login', userMessage='Please Login')

# Logout route
# curl http://127.0.0.1:5000/logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

########################################################################
#get all locs
@app.route('/locations')
def getAllLocs():
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.getAllLocs())

#get all depts
@app.route('/departments')
def getAllDepts():
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.getAllDepts())

#get all emps
@app.route('/employees')
def getAllEmps():
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.getAllEmps())

#get all users
@app.route('/users')
def getAllUsers():
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.getAllUser())
#########################################################################

#find by id
#for all tables

#locations
#curl
#curl http://127.0.0.1:5000/locations/1
@app.route('/locations/<int:locID>')
def findLocById(locID):
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.findLocById(locID))

#departments
#curl
#curl http://127.0.0.1:5000/departments/5
@app.route('/departments/<int:deptID>')
def findDeptById(deptID):
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.findDeptById(deptID))

@app.route('/departmentname/<int:deptID>')
def findDeptNameById(deptID):
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.findDeptById(deptID))

#employees
#curl
#curl http://127.0.0.1:5000/employees/5
@app.route('/employees/<int:empID>')
def findEmpById(empID):
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.findEmpById(empID))

#users
#curl
#curl http://127.0.0.1:5000/users/1
@app.route('/users/<int:userID>')
def findUserById(userID):
    if not 'username' in session:
        abort(401)
    return jsonify(orgDao.findUserByID(userID))
#########################################################################

#create for all tables

#create locations
#curl
#curl -X POST -d "{\"location\":\"test\", \"type\":\"rented or leased\", \"years_occupancy\":123}" -H "Content-Type:application/json" http://127.0.0.1:5000/locations
@app.route('/locations', methods=['POST'])
def createLoc():
    if not 'username' in session:
        abort(401)

    if not request.json:
        abort(400)

    location = {
        "loc_name": request.json["loc_name"],
        "type": request.json["type"],
        "years_occupancy": request.json["years_occupancy"]
    }
    return jsonify(orgDao.createLocation(location))

#create dept
#curl
#curl -X POST -d "{\"dept_name\":\"test\", \"budget\":99999, \"location\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/departments
@app.route('/departments', methods=['POST'])
def createDept():
    if not 'username' in session:
        abort(401)
    if not request.json:
        abort(400)

    department = {
        "dept_name": request.json["dept_name"],
        "budget": request.json["budget"],
        "location": request.json["location"]
        }
    try:
        new_dept = orgDao.createDepartment(department)
        return jsonify(new_dept)
    except:
        app.logger.info('LocID does not Exist')
        return jsonify({"done":False})

#create employee
#curl
#curl -X POST -d "{\"name\":\"test\", \"title\":\"testtitle\",\"salary\":99999, \"dept\":2}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def createEmp():
    if not 'username' in session:
        abort(401)
    
    if not request.json:
        abort(400)
        
    employee = {
            "name": request.json["name"],
            "title": request.json["title"],
            "salary":request.json["salary"],
            "dept": request.json["dept"]
        }
    
    try:
        new_emp = orgDao.createEmployee(employee)
        return jsonify(new_emp)
    except:
        app.logger.info('DeptID does not Exist')
        return jsonify({"done":False})
    


#create user
#curl
#curl -X POST -d "{\"name\":\"test\", \"password\":\"test user\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/login
@app.route('/users', methods=['POST'])
def createUser():
    if not 'username' in session:
        abort(401)

    if not request.json:
        abort(400)

    user = {
        "name": request.json["name"],
        "password": request.json["password"]
    }
    return jsonify(orgDao.createUser(user))

############################################################
# Update

# update locations
# curl
# curl -X PUT -d "{\"location\":\"new Name\", \"years_occupancy\":999}" -H "content-type:application/json" http://127.0.0.1:5000/locations/2
@app.route('/locations/<int:locID>', methods=['PUT'])
def updateLoc(locID):
    if not 'username' in session:
        abort(401)
    if not request.json:
        abort(400)

    foundLoc = orgDao.findLocById(locID)

    if foundLoc == {}:
        app.logger.info('LocID %s not found', locID)
        return jsonify({}),404

    currentLoc = foundLoc
    if 'loc_name' in request.json:
        currentLoc['loc_name'] = request.json['loc_name']
    if 'type' in request.json:
        currentLoc['type'] = request.json['type']
    if 'years_occupancy' in request.json:
        currentLoc['years_occupancy'] = request.json['years_occupancy']
    orgDao.updateLoc(currentLoc)

    return jsonify(currentLoc)

# update departments
# curl
# curl -X PUT -d "{\"dept_name\":\"mad crowd\"}" -H "content-type:application/json" http://127.0.0.1:5000/departments/59
@app.route('/departments/<int:deptID>', methods=['PUT'])
def updateDept(deptID):
    if not 'username' in session:
        abort(401)

    if not request.json:
      abort(400)

    foundDept = orgDao.findDeptById(deptID)
    if foundDept == {}:
        app.logger.info('DepID %s not found', deptID)
        return jsonify({}),404
        
    currentDept = foundDept

    if 'dept_name' in request.json:
        currentDept['dept_name'] = request.json['dept_name']
    if 'budget' in request.json:
        currentDept['budget'] = request.json['budget']
    if 'location' in request.json:
        locID = request.json['location']
        checkLoc = orgDao.findLocById(locID)

        if checkLoc == {}:
            return jsonify({}),404
        currentDept['location'] = locID
    orgDao.updateDept(currentDept)
    return jsonify(currentDept)


# update employees
# curl
# curl -X PUT -d "{\"title\":\"mad manager\",\"salary\":15000}" -H "content-type:application/json" http://127.0.0.1:5000/employees/21
@app.route('/employees/<int:empID>', methods=['PUT'])
def updateEmp(empID):
    if not 'username' in session:
        abort(401)
    if not request.json:
        abort(400)
    foundEmp = orgDao.findEmpById(empID)
    if foundEmp == {}:
        app.logger.info('EmpID %s not found', empID)
        return jsonify({}), 404
    currentEmp = foundEmp
    if 'name' in request.json:
        currentEmp['name'] = request.json['name']
    if 'address' in request.json:
        currentEmp['title'] = request.json['title']
    if 'title' in request.json:
        currentEmp['salary'] = request.json['salary']
    if 'dept' in request.json:
        deptID = request.json['dept']
        checkDept = orgDao.findDeptById(deptID)
        if checkDept == {}:
            return jsonify({}), 404
        currentEmp['dept'] = deptID
    orgDao.updateEmp(currentEmp)
    return jsonify(currentEmp)

# update users
# curl
# curl -X PUT -d "{\"password\":\"abc123\"}" -H "content-type:application/json" http://127.0.0.1:5000/login/7
@app.route('/users/<int:userID>', methods=['PUT'])
def updateUser(userID):
    if not 'username' in session:
        abort(401)
    foundUser = orgDao.findUserByID(userID)
    if foundUser == {}:
        return jsonify({}), 404
    currentUser = foundUser
    if 'name' in request.json:
        currentUser['name'] = request.json['name']
    if 'password' in request.json:
        currentUser['password'] = request.json['password']
    orgDao.updateUser(currentUser)

    return jsonify(currentUser)

###############################################################
#Delete

# delete location
#curl
# curl -X DELETE http://127.0.0.1:5000/locations/2
@app.route('/locations/<int:locID>', methods=['DELETE'])
def deleteLoc(locID):
    if not 'username' in session:
        abort(401)
    foundLoc = orgDao.findLocById(locID)
    if foundLoc == {}:
        app.logger.info('LocID %s not found', locID)
        return jsonify({"done": False}), 404
    
    try:
        orgDao.deleteLoc(locID)
        app.logger.info('Deleted loc %s', foundLoc)
        return jsonify({"done":True})
    except:
        app.logger.info('Cannot delete LocID %s', locID)
        return jsonify({"done":False})

# delete department
#curl
# curl -X DELETE http://127.0.0.1:5000/departments/2
@app.route('/departments/<int:deptID>', methods=['DELETE'])
def deleteDept(deptID):
    if not 'username' in session:
        abort(401)
    
    foundDept = orgDao.findDeptById(deptID)
    
    if foundDept == {}:
        app.logger.info('DeptID %s not found', deptID)
        return jsonify({"done": False}), 404

    try:
        orgDao.deleteDept(deptID)
        app.logger.info('Deleted dept %s', foundDept)
        return jsonify({"done":True})
    except:
        app.logger.info('Cannot delete deptID %s', deptID)
        return jsonify({"done":False})


# delete employee
#curl
# curl -X DELETE http://127.0.0.1:5000/employees/23
@app.route('/employees/<int:empID>', methods=['DELETE'])
def deleteEmployee(empID):
    if not 'username' in session:
        abort(401)

    foundEmp = orgDao.findEmpById(empID)
    if foundEmp == {}:
        app.logger.info('EmpID %s not found', empID)
        return jsonify({"done": False}), 404
    
    orgDao.deleteEmp(empID)
    return jsonify({"done": True})

# delete user
# curl
# curl -X DELETE http://127.0.0.1:5000/login/7
@app.route('/users/<int:userID>', methods=['DELETE'])
def deleteUser(userID):
    if not 'username' in session:
        abort(401)
    orgDao.deleteUser(userID)

    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)