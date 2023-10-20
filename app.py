from flask import Flask, jsonify, request

app = Flask(__name__)



students = {
        '1': {  'name': 'Alice', 'grade': 'A'},
        '2': {  'name': 'Bob', 'grade': 'B+'}
    }

@app.route('/')
def hello():
    return students

@app.route('/student/<id>')
def student(id):
    
    student_info = students.get(id, {})
    if(len(student_info.keys())) == 0:
        # try once more with string user id
        string_student_info = students.get(str(id),{})
        if(len(string_student_info.keys()) == 0):
            return 'No user found',404
        else:
            return jsonify(string_student_info) 
    else:
        return jsonify(student_info)




# CREATE OPERATION
@app.route('/student/add',methods=['POST'])
def student_add():
    
    if(request.json['name'] and request.json['id'] and request.json['grade']):
        # code here
        if(request.json['name'] !='' and request.json['id'] != '' and request.json['grade'] != ''):
    
            name = request.json['name']
            
            grade = request.json['grade']
            
            
            new_key = int(sorted(students.keys())[-1]) + 1

            students[f'{new_key}'] = {
                "name" : name,
                "grade" : grade
            }
            return jsonify(students)
        else:
            return 'parameters missing'
    else:
        return 'parameteres missing'


# UPDATE OPERATION
@app.route('/student/update_student', methods=['PUT', 'POST'])
def update():
    if(request.method == 'POST' or request.method == 'PUT'):
    
        if(request.json['id']):
            if(students.get(str(request.json['id']), {})):
                

                id = str(request.json['id'])
                grade = request.json['grade']
                name = request.json['name']
                    
                students[f'{id}'] = {
                    "grade" : grade,
                    "name" : name
                }
                return students[f'{id}']
            else: 
                return "Student not found"
        else:
            return 'Student not found'
        
    else:
        return 'method not allowed',403

# DELETE OPERATION

@app.route('/student/delete_student', methods=['DELETE'])
def delete():
    
   
    if(request.method == 'DELETE'):
        
        if(students.get(str(request.json['id']), {})):
            
            students.pop(str(request.json['id']))        
            return {
                "message" : "student deleted",
                "remaninig_students" : students
            }
        else:
            return 'student does not exist'
    else:
        return 'method not allowed',403


def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)