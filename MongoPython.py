from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['myDatabase']
collection = db['students']


def create_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    courses = input("Enter student courses (comma-separated): ").split(',')
    student_data = {
        "name": name,
        "age": age,
        "courses": courses
    }
    result = collection.insert_one(student_data)
    print(f"Student inserted with ID: {result.inserted_id}")


def read_students():
    students = collection.find()
    print("\nList of students:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Courses: {', '.join(student['courses'])}")


def update_student():
    name = input("Enter the student name to update: ")
    new_age = int(input("Enter the new age: "))
    result = collection.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
    )
    if result.matched_count > 0:
        print(f"Student '{name}' updated successfully.")
    else:
        print(f"Student '{name}' not found.")


def delete_student():
    name = input("Enter the student name to delete: ")
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Student '{name}' deleted successfully.")
    else:
        print(f"Student '{name}' not found.")

def find_student():
    name = input("Enter the name of the student to find: ")
    student = collection.find_one({"name": name})
    if student:
        print(f"\nStudent found: Name: {student['name']}, Age: {student['age']}, Courses: {', '.join(student['courses'])}")
    else:
        print(f"No student found with the name '{name}'.")

def menu():
    while True:
        print("\n--- MongoDB CRUD Operations ---")
        print("1. Insert Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Find Student by Name")
        print("6. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_student()
        elif choice == '2':
            read_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            find_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()

    
    client.close()
