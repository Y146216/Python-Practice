import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yashu@123",
        database="student_db"
    )

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Marks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be empty")
        else:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name) VALUES (%s)",
                (name,)
            )
            conn.commit()
            conn.close()
            print("Student added successfully")

    elif choice == "2":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM students")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("No students found")
        else:
            print("\nStudents:")
            for row in rows:
                print(row[0], "-", row[1])
            
    elif choice == "3":
       id = input("Enter student ID to delete: ").strip()

       if not id.isdigit():
        print("Invalid ID")
       else:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = %s",
            (int(id),)
        )

        if cursor.rowcount == 0:
            print("No student found with this ID")
        else:
            conn.commit()
            print("Student deleted successfully")

        conn.close()

    elif choice == "4":
        id = input("Enter student ID: ").strip()
        new_marks = input("Enter new marks: ").strip()

        if not id.isdigit() or not new_marks.isdigit():
         print("Invalid input")
        else:
         conn = get_connection()
         cursor = conn.cursor()

         cursor.execute(
            "UPDATE students SET marks = %s WHERE id = %s",
            (int(new_marks), int(id))
        )

        if cursor.rowcount == 0:
            print("No student found with this ID")
        else:
            conn.commit()
            print("Marks updated successfully")

        conn.close()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
