import requests

def printMenu():
    print("1. get all students")
    print("2. get a student by id")
    print("3. save new student")
    print("4. change student name")
    print("5. change student age")
    print("6. delete student")
    print("7. exit")
    return input("Enter your choice: ")

def setServerURL(ip: str, port :str) -> str:
    URL = f'http://{ip}:{port}/'
    return URL
    return f'http://{ip}:{port}/'


def main():
    while True:
        ip = input("Enter server ip: ")
        port = input("Enter server port: ")
        response = requests.get(f'http://{ip}:{port}/')
        print(response.text)
        if response.text == 'Welcome to the Students API':
            server_enpoint = setServerURL(ip, port)
            choice = printMenu()
            if choice == '1':
                response = requests.get(server_enpoint+'students')
                students = response.json()
                if students:
                    print("\nAll Students:")
                    print("-" * 30)
                    for student in students:
                        print(f"ID: {student['id']}")
                        print(f"Name: {student['name']}")
                        print(f"Age: {student['age']}")
                        print("-" * 30)
                else:
                    print("No students found.")

            elif choice == '2':
                id = input("Enter student id: ")
                response = requests.get(server_enpoint+'student', params={'id': id})
                print(response.json())
            elif choice == '3':
                name = input("Enter student name: ")
                age = input("Enter student age: ")
                response = requests.post(server_enpoint+'student', json={'name': name, 'age': age})
                print(response.json())
            elif choice == '4':
                id = input("Enter student id: ")
                name = input("Enter new name: ")
                response = requests.put(server_enpoint+'student/editname', json={'id': id, 'name': name})
                print(response.json())
            elif choice == '5':
                id = input("Enter student id: ")
                age = input("Enter new age: ")
                response = requests.put(server_enpoint+'student/editage', json={'id': id, 'age': age})
                print(response.json())
            elif choice == '6':
                name = input("Enter student name: ")
                response = requests.delete(server_enpoint+'student', json={'name': name})
                print(response.json())
            elif choice == '7':
                input ('are you sure you want to exit?(y/n)')