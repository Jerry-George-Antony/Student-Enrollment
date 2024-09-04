import mysql.connector
from datetime import date

# Establish connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',  # Replace with your MySQL username
    password='password',  # Replace with your MySQL password
    database='StudentEnrollmentDB'
)

cursor = connection.cursor()

# Function to add a new student
def add_student(first_name, last_name, email, phone_number):
    sql = "INSERT INTO Students (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, email, phone_number)
    cursor.execute(sql, values)
    connection.commit()
    print("Student added successfully!")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM Students")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to enroll a student in a course
def enroll_student(student_id, course_id):
    enrollment_date = date.today()
    sql = "INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
    values = (student_id, course_id, enrollment_date)
    cursor.execute(sql, values)
    connection.commit()
    print("Student enrolled successfully!")

# Function to view all enrollments
def view_enrollments():
    sql = """
    SELECT Students.first_name, Students.last_name, Courses.course_name, Enrollments.enrollment_date
    FROM Enrollments
    JOIN Students ON Enrollments.student_id = Students.student_id
    JOIN Courses ON Enrollments.course_id = Courses.course_id
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Menu options for interacting with the system
def menu():
    while True:
        print("\nStudent Enrollment System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Enroll Student in a Course")
        print("4. View All Enrollments")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            add_student(first_name, last_name, email, phone_number)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            enroll_student(student_id, course_id)
        elif choice == '4':
            view_enrollments()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()

# Close the database connection
cursor.close()
connection.close()
