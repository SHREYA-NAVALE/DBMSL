import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",   
        user="root",        
        password="Shreya:)",
        database="SQLPython" 
    )  

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            grade VARCHAR(10)
        )
    """)
    conn.commit()
    print("Table 'students' created successfully.")

def create_student(conn):
    cursor = conn.cursor()
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    print(f"Student '{name}' inserted successfully.")

def read_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\nList of Students:")
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade'}")
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]}")
    if not rows:
        print("No records found.")

def find_student(conn):
    cursor = conn.cursor()
    name = input("Enter the student name to search: ")

    query = "SELECT * FROM students WHERE name = %s"
    cursor.execute(query, (name,))
    rows = cursor.fetchall()

    if rows:
        print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Grade'}")
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]}")
    else:
        print(f"No student found with the name '{name}'.")

def update_student(conn):
    cursor = conn.cursor()
    student_id = int(input("Enter the student ID to update: "))
    new_age = int(input("Enter the new age: "))
    new_grade = input("Enter the new grade: ")

    query = "UPDATE students SET age = %s, grade = %s WHERE id = %s"
    cursor.execute(query, (new_age, new_grade, student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"Student ID {student_id} not found.")

def delete_student(conn):
    cursor = conn.cursor()
    student_id = int(input("Enter the student ID to delete: "))
    
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"Student ID {student_id} not found.")

def menu():
    conn = connect_to_db()
    create_table(conn)  

    while True:
        print("\n--- MySQL CRUD Operations ---")
        print("1. Insert Student")
        print("2. View All Students")
        print("3. Find Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            create_student(conn)
        elif choice == '2':
            read_students(conn)
        elif choice == '3':
            find_student(conn)
        elif choice == '4':
            update_student(conn)
        elif choice == '5':
            delete_student(conn)
        elif choice == '6':
            print("Exiting...")
            conn.close()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
