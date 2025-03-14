from flask import Flask, request, jsonify

app = Flask(__name__)
id_counter = 3
students = {
    '0': {
        'id': 0,
        'name': 'John',
        'age': 21,
    },
    '1': {
        'id': 1,
        'name': 'Jane',
        'age': 22,
    },
    '2': {
        'id': 2,
        'name': 'Doe',
        'age': 23,
 }
}

@app.route('/', methods=['GET']) # just to check if the server is running
def check():
    return 'Welcome to the Students API'



@app.route('/students', methods=['GET'])# get all students
def get_students():
    return jsonify(students)

@app.route('/student/<id>', methods=['GET'])# get a student by id
def get_student(id):
    try:
        if id in students:
            return jsonify(students[id])
        return jsonify({'error': 'Student not found'}),404
    except:
        return jsonify({'error': 'Invalid request get a specific student'}),400
    
@app.route('/student', methods=['POST'])# add a student
def add_student():
    try:
        global id_counter  # Add this line
        student = {
            'id': id_counter,
            'name': request.json['name'],
            'age': request.json['age'],
        }
        students[f'{id_counter}'] = student
        id_counter += 1
        return jsonify(student)
    except:
        return jsonify({'error': 'Invalid request to create a new student'}),400


@app.route('/student/editage/<id>', methods=['PUT'])# update student age
def update_student_age(id):
    try:
        student = students[id]
        student['age'] = request.json['age']
        return jsonify(student)
    except:
        return jsonify({'error': 'Student not found'}),404

@app.route('/student/editname/<id>', methods=['PUT'])# update student name
def update_student_name(id):
    try:
        student = students[id]
        student['name'] = request.json['name']
        return jsonify(student)
    except:
        return jsonify({'error': 'Student not found'}),404

@app.route('/student/<id>', methods=['DELETE'])# delete a student
def delete_student(id):
    try:
        del students[id]
        return jsonify({'message': 'Student deleted'})
    except:
        return jsonify({'error': 'Student not found so it cannot be deleted'}),404
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 5001)
