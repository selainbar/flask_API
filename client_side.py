import requests

def printMenu():
    print("1. get all students")
    print("2. get a student by id")
    print("3. save new student")
    print("4. change student name")
    print("5. change student age")
    print("6. delete student")
    print("7. exit")
    user_input = input("Enter your choice: ")
    user_input = inputIsDigit(user_input)
    return user_input

def inputIsDigit(input) -> int:
    while True:
        if input.isdigit():
            return int(input)
        else:
            print("Please enter a number")
            input = input("Enter your choice: ")


def setServerURL(ip: str, port :str) -> str:
    URL = f'http://{ip}:{port}/'
    return URL

def printStudents(students):
    print("\nAll Students:")
    print("-" * 30)
    for student in students:
        print(student)
        print("-" * 30)

def printStudent(student):
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print("-" * 30)

def main():
    while True:
        ip = input("Enter server ip: ")
        port = input("Enter server port: ")
        response = requests.get(f'http://{ip}:{port}/')
        print(response.text)
        if response.text == 'Welcome to the Students API':
            server_enpoint = setServerURL(ip, port)
            choice = printMenu()
            if choice == 1:
                response = requests.get(server_enpoint+'students')
                students = response.json()
                if students:
                    printStudents(students)
                else:
                    print("No students found")
            elif choice == 2:
                id = input("Enter student id: ")
                response = requests.get(server_enpoint+'student', params={'id': id})
                if response.json():
                    printStudent(response.json())
                else:
                    print('Student not found')
            elif choice == 3:
                name = input("Enter student name: ")
                age = input("Enter student age: ")
                response = requests.post(server_enpoint+'student', json={'name': name, 'age': age})
                if response.json():
                    print('student was saved')
                else:
                    print('student was not saved because of the error: \n', response.json()['error'])

            elif choice == 4:
                id = input("Enter student id: ")
                name = input("Enter new name: ")
                response = requests.put(server_enpoint+'student/editname', json={'id': id, 'name': name})
                if response.json():
                    print("the student's name was changed")
            elif choice == 5:
                id = input("Enter student id: ")
                age = input("Enter new age: ")
                response = requests.put(server_enpoint+'student/editage', json={'id': id, 'age': age})
                if response.json():
                    print("the student's age was changed")
                else:
                    print(response.json()['error'])
            elif choice == 6:
                name = input("Enter student name: ")
                response = requests.delete(server_enpoint+'student', json={'name': name})
                if response.json():
                    print("the student was deleted")
                else:
                    print('student was not deleted because of the error: \n', response.json()['error'])
            elif choice == 7:
                input ('are you sure you want to exit?(y/n)')

if __name__ == '__main__':
    main()

