students = []

while True:
 print("\n===== Student Management System =====")
 print("1. Add Student")
 print("2. View Students")
 print("3. Exit")

 choice = input("Enter your choice: ")

 if choice == "1":
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty")
    else:
        students.append(name)
        print("Student added successfully")

 elif choice == "2":
    if not students:
        print("No students found")
    else:
        print("Students:")
        for student in students:
            print("-", student)

 elif choice == "3":
     print("exiting the program")

 else :
     print("invalid choice")