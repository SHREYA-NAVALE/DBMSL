import mysql.connector
# import pandas as pd

# Function to connect to the database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Corrected from 'root' to 'user' for MySQL connection
        password="Shreya:)",
        database="Sqlmongotest"
    )

# Function to create a table
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT,
            grade VARCHAR(50)
        )
    """)
    conn.commit()
    print("Table created successfully!")

# Function to insert a student record
def insert_student(conn):
    cursor = conn.cursor()
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    query = "INSERT INTO student (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    print(f"Inserted {cursor.rowcount} record(s) into the student table.")

# Function to read all student records
def read_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("Students in the database:")
    for row in rows:
        print(row)
    if not rows:
        print("No records found.")

# Function to update a student record
def update_student(conn):
    cursor = conn.cursor()
    student_id = int(input("Enter the student ID to update: "))
    new_age = int(input("Enter the new age: "))
    new_grade = input("Enter the new grade: ")
    query = "UPDATE student SET age = %s, grade = %s WHERE id = %s"
    cursor.execute(query, (new_age, new_grade, student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"Student ID {student_id} not found.")

# Function to find a student by name
def find_student(conn):
    cursor = conn.cursor()
    name = input("Enter name to search: ")
    query = "SELECT * FROM student WHERE name = %s"
    cursor.execute(query, (name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("No records found.")

# Function to delete a student record
def delete_student(conn):
    cursor = conn.cursor()
    student_id = int(input("Enter the student ID to delete: "))
    query = "DELETE FROM student WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"Student ID {student_id} not found.")

# Main function with menu to demonstrate CRUD operations
def menu():
    conn = create_connection()
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
            insert_student(conn)
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