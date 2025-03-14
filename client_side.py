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
    try:
        print("\nAll Students:")
        print("-" * 30)
        for student in students.values():
            print(f"Student id: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print("-" * 30)
    except:
        print("Students not found")
        
def printStudent(student):
    try:
        print("\nStudent:")
        print("-" * 30)
        print(f"Student id: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print("-" * 30)
    except:
        print("Student not found")
        print("-" * 30)


def main():
    ip = input("Enter server ip: ")
    port = input("Enter server port: ")
    response = requests.get(f'http://{ip}:{port}/')
    print(response.text)
    if response.text == 'Welcome to the Students API':
        server_enpoint = setServerURL(ip, port)
    while True:
            try:
                choice = printMenu()
                if choice == 1:
                    response = requests.get(server_enpoint+'students')
                    students = response.json()
                    if response.status_code == 200:
                        printStudents(students)
                    else:
                        print("-" * 30)
                        print(response.json()['error'])
                        print("-" * 30)
                elif choice == 2:
                    id = input("Enter student id: ")
                    response = requests.get(server_enpoint+f'student/{id}')
                    if response.status_code == 200:
                        printStudent(response.json())
                    else:
                        print("-" * 30)
                        print(response.json()['error'])
                        print("-" * 30)
                elif choice == 3:
                    name = input("Enter student name: ")
                    age = input("Enter student age: ")
                    response = requests.post(server_enpoint+'student', json={'name': name, 'age': age})
                    if response.status_code == 200:
                        print("-" * 30)
                        print('student was saved')
                        print("-" * 30)
                    else:
                        print("-" * 30)
                        print(response.json()['error'])
                        print("-" * 30)
                elif choice == 4:
                    id = input("Enter student id: ")
                    name = input("Enter new name: ")
                    response = requests.put(server_enpoint+f'student/editname/{id}', json={'name': name})
                    if response.status_code == 200:
                        print("-" * 30)
                        print("the student's name was changed")
                        print("-" * 30)
                    else:
                        print("-" * 30)
                        print(response.json()['error'])
                        print("-" * 30)
                elif choice == 5:
                    id = input("Enter student id: ")
                    age = input("Enter new age: ")
                    response = requests.put(server_enpoint+f'student/editage/{id}', json={'age': age})
                    if response.status_code == 200:
                        print("-" * 30)
                        print("the student's age was changed")
                        print("-" * 30)
                    else:
                        print("-" * 30)
                        print(response.json()['error'])
                        print("-" * 30)
                elif choice == 6:
                    name = input("Enter student id: ")
                    response = requests.delete(server_enpoint+f'student/{id}')
                    if response.status_code == 200:
                        print("-" * 30)
                        print("the student was deleted")
                        print("-" * 30)
                    else:
                        print("-" * 30)
                        print(response.json()['error'])
                        print("-" * 30)
                elif choice == 7:
                    user_input = input ('are you sure you want to exit?(y/n)')
                    if user_input == 'y':
                        break
                else:
                    print("Invalid choice")
            except Exception as e:
                print("An error occurred")
                print(e)
if __name__ == '__main__':
    main()

