from flask import Flask, url_for, request, redirect, abort, jsonify
from DAO import orgDao


app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

#get all locs
@app.route('/locations')
def getAllLocs():
    return jsonify(orgDao.getAllLocs())
    #return orgDao.getAllLocs

#get all depts
@app.route('/departments')
def getAllDepts():
    return jsonify(orgDao.getAllDepts())

#get all emps
@app.route('/employees')
def getAllEmps():
    return jsonify(orgDao.getAllEmps())

#find by id
#for all tables

#locations
#curl
#curl http://127.0.0.1:5000/locations/1
@app.route('/locations/<int:locID>')
def findLocById(locID):
    return jsonify(orgDao.findLocById(locID))

#departments
#curl
#curl http://127.0.0.1:5000/departments/5
@app.route('/departments/<int:deptID>')
def findDeptById(deptID):
    return jsonify(orgDao.findDeptById(deptID))

#employees
#curl
#curl http://127.0.0.1:5000/employees/5
@app.route('/employees/<int:empID>')
def findEmpById(empID):
    return jsonify(orgDao.findEmpById(empID))


#create for all tables

#create locations
#curl
#curl -X POST -d "{\"location\":\"test\", \"type\":\"rented or leased\", \"years_occupancy\":123}" -H "Content-Type:application/json" http://127.0.0.1:5000/locations
@app.route('/locations', methods=['POST'])
def createLoc():
  
    if not request.json:
        abort(400)

    location = {
        "location": request.json["location"],
        "type": request.json["type"],
        "years_occupancy": request.json["years_occupancy"]
    }
    return jsonify(orgDao.createLocation(location))

#create dept
#curl
#curl -X POST -d "{\"dept_name\":\"test\", \"budget\":99999, \"location\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/departments
@app.route('/departments', methods=['POST'])
def createDept():
    try:
        if not request.json:
            abort(400)
            
        department = {
            "dept_name": request.json["dept_name"],
            "budget": request.json["budget"],
            "location": request.json["location"]
        }
        return jsonify(orgDao.createDepartment(department))

    except Exception as e:
        e = 'Cannot add or update a child row\nLocation ID does not Exist\nForeign key constraint fails'
        return str(e)


#create employee
#curl
#curl -X POST -d "{\"name\":\"test\", \"title\":\"testtitle\",\"salary\":99999, \"dept\":2}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def createEmp():
    try:
        if not request.json:
            abort(400)
            
        employee = {
            "name": request.json["name"],
            "title": request.json["title"],
            "salary":request.json["salary"],
            "dept": request.json["dept"]
        }
        return jsonify(orgDao.createEmployee(employee))

    except Exception as e:
        e = 'Cannot add or update a child row\nLocation ID does not Exist\nForeign key constraint fails'
        return str(e)
       

if __name__ == "__main__":
    app.run(debug=True)