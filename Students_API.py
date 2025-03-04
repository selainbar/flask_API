from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {
        'name': 'John Doe',
        'age': 20,
    },
    {
        'name': 'Jane Doe',
        'age': 21,
    }
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/student', methods=['GET'])
def get_student():
    name = request.args.get('name')
    for student in students:
        if student['name'] == name:
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

@app.route('/student', methods=['POST'])
def add_student():
    student = {
        'name': request.json['name'],
        'age': request.json['age'],
    }
    students.append(student)
    return jsonify(student)

@app.route('/student', methods=['PUT'])
def update_student():
    name = request.json['name']
    for student in students:
        if student['name'] == name:
            student['age'] = request.json['age']
            return jsonify(student)
    return jsonify({'error': 'Student not found'})

@app.route('/student', methods=['DELETE'])
def delete_student():
    name = request.json['name']
    for student in students:
        if student['name'] == name:
            students.remove(student)
            return jsonify(student)
    return jsonify({'error': 'Student not found'})


if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 5001)
