import mysql.connector

# Establishing MySQL connection
db= mysql.connector.connect(host='localhost', user='root', password='1234')

cur= db.cursor()

#Creating database if not Exists
query="CREATE DATABASE IF NOT EXISTS school_management"
cur.execute(query)
cur.execute("USE school_management")


#creating student table
cur.execute("CREATE TABLE IF NOT EXISTS students (admission_no INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255),last_name VARCHAR(255),class VARCHAR(50),dob DATE,address VARCHAR(255),contact_no VARCHAR(15),status ENUM('Active', 'Left'))")

cur.execute("CREATE TABLE IF NOT EXISTS left_students (admission_no INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255),last_name VARCHAR(255),class VARCHAR(50),dob DATE,address VARCHAR(255),contact_no VARCHAR(15),status ENUM('Active', 'Left'))")

#Creating Table for Teacher
cur.execute("CREATE TABLE IF NOT EXISTS teachers ( teacher_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50),last_name VARCHAR(50),contact_number VARCHAR(15),qualification VARCHAR(100),subjects VARCHAR(100),designation VARCHAR(50),status ENUM('Active', 'Left'))")

cur.execute("CREATE TABLE IF NOT EXISTS left_teachers ( teacher_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50),last_name VARCHAR(50),contact_number VARCHAR(15),qualification VARCHAR(100),subjects VARCHAR(100),designation VARCHAR(50),status ENUM('Active', 'Left'))")

#----------------------------FUNCTION RELATED TO STUDENT PANNEL--------------------------------

#Regester Student

def register_student():
    print()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    class_name = input("Enter class: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    address = input("Enter address: ")
    contact_no = input("Enter contact number: ")
    print()

    insert_query = "INSERT INTO students (first_name, last_name, class, dob, address, contact_no, status) VALUES (%s, %s, %s, %s,%s,%s, 'Active')"
    cur.execute(insert_query, (first_name, last_name, class_name, dob, address, contact_no))
    db.commit()
    
    print("\nStudent registered successfully.\n")
    
#Edit Detail Of Existing student

def edit_student():
    print()
    admission_no = int(input("Enter Admission Number of the student to edit: "))
    print()
    
    select_query = "SELECT * FROM students WHERE admission_no = %s"
    cur.execute(select_query, (admission_no,))
    student = cur.fetchone()

    if student is None:
        print("Student not found.")
        return

    print(f"Editing details for student with Admission Number {admission_no}:")
    first_name = input(f"Enter new first name (currently: {student[1]}): ")
    last_name = input(f"Enter new last name (currently: {student[2]}): ")
    class_name = input(f"Enter new class (currently: {student[3]}): ")
    dob = input(f"Enter new date of birth (YYYY-MM-DD) (currently: {student[4]}): ")
    address = input(f"Enter new address (currently: {student[5]}): ")
    contact_no = input(f"Enter new contact number (currently: {student[6]}): ")

    update_query = """UPDATE students SET 
                    first_name = %s, 
                    last_name = %s, 
                    class = %s, 
                    dob = %s, 
                    address = %s, 
                    contact_no = %s 
                    WHERE admission_no = %s """
                    
    cur.execute(update_query, (first_name, last_name, class_name, dob, address, contact_no, admission_no))
    db.commit()
    print(f"Student details for Admission Number {admission_no} updated successfully.")

#Delete Data of Existing Student

def delete_student():
    print()
    admission_no = int(input("Enter Admission Number of the student to delete: "))
    
    select_query = "SELECT * FROM students WHERE admission_no = %s"
    cur.execute(select_query, (admission_no,))
    student = cur.fetchone()

    if student is None:
        print("\nStudent not found.\n")
        return

    # Move the student to the 'Left' status and create a record in the 'left_students' table
    insert_left_query = """INSERT INTO left_students (
        admission_no, 
        first_name, 
        last_name, 
        class, dob, 
        address, 
        contact_no)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(insert_left_query, student[0:7])
    
    delete_query = "DELETE FROM students WHERE admission_no = %s"
    cur.execute(delete_query, (admission_no,))
    db.commit()
    print(f"Student with Admission Number {admission_no} has been deleted and moved to the 'Left' records.")
    
#To Show all Students Data

def show_students(status='Active'):
    select_query = "SELECT * FROM students WHERE status = %s"
    cur.execute(select_query, (status,))
    students = cur.fetchall()

    print(f"{'Admission No':<15}{'First Name':<15}{'Last Name':<15}{'Class':<10}\t{'Date of Birth'}\t{'Address'}\t{'Contact No':<15}")
    for student in students:
        print(f"{student[0]:<15}{student[1]:<15}{student[2]:<15}{student[3]:<10}\t{student[4]}\t{student[5]}\t{student[6]}")

#-------------------------------------FUNCTION RELATED TO STUDENT PANNEL-------------------------------------

#Teacher Regestration
def register_teacher():
    
    print("Teacher Registration")
    
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    contact_number = input("Enter contact number: ")
    qualification = input("Enter highest qualification: ")
    subjects = input("Enter subjects to teach (comma-separated): ")
    designation = input("Enter designation: ")
    

    insert_query = "INSERT INTO teachers (first_name, last_name, contact_number, qualification, subjects, designation) VALUES (%s,%s, %s, %s, %s, %s)"
    
    values = (first_name, last_name, contact_number, qualification, subjects, designation)

    cur.execute(insert_query, values)
    db.commit()
    
    print("\nTeacher registered successfully!\n")

#Edit Detail of Existing Teacher

def edit_teacher():
    print()
    teacher_id = int(input("Enter the teacher ID you want to edit: "))
    print()
    
    select_query = "SELECT * FROM teachers WHERE teacher_id = %s"
    cur.execute(select_query, (teacher_id,))
    teacher = cur.fetchone()

    if teacher is None:
        print("Teacher not found.")
        return
    
    print(f"Editing details for teacher with Teacher ID {teacher_id}:")
    first_name = input(f"Enter new first name (currently: {teacher[1]}): ")
    last_name = input(f"Enter new last name (currently: {teacher[2]}): ")
    contact_number = input(f"Enter new contact number: (currently: {teacher[3]}): ")
    qualification = input(f"Enter new highest qualification: (currently: {teacher[4]}): ")
    subjects = input(f"Enter new subjects to teach (comma-separated): (currently: {teacher[5]}): ")
    designation = input(f"Enter new designation: (currently: {teacher[6]}): ")

    update_query = "UPDATE teachers SET first_name = %s, last_name = %s, contact_number = %s, qualification = %s, subjects = %s, designation = %s WHERE teacher_id = %s"
    values = (first_name, last_name, contact_number, qualification, subjects, designation, teacher_id)

    cur.execute(update_query, values)
    db.commit()
    print(f"Teacher with ID {teacher_id} has been updated.")

#Deleting existing data of Teacher
def delete_teacher():
    print()
    teacher_id = int(input("Enter Admission Number of the student to delete: "))
    
    select_query = "SELECT * FROM teachers WHERE teacher_id = %s"
    cur.execute(select_query, (teacher_id,))
    teacher = cur.fetchone()

    if teacher is None:
        print("\nTeacher not found.\n")
        return

    # Move the teacher to the 'Left' status and create a record in the 'left_teachers' table
    insert_left_query = """INSERT INTO left_teachers (
        teacher_id,
        first_name, 
        last_name, 
        contact_number, 
        qualification, 
        subjects, 
        designation (%s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(insert_left_query, teacher[0:7])
    
    delete_query = "DELETE FROM teachers WHERE teacher_id= %s"
    cur.execute(delete_query, (teacher_id,))
    db.commit()
    print(f"Teacher with teacher_id {teacher_id} has been deleted and moved to the 'Left' records.")
    
#To Show All Data Of Teachers
def show_teachers(status='Active'):
    select_query = "SELECT * FROM teachers WHERE status = %s"
    cur.execute(select_query, (status,))
    teachers = cur.fetchall()

    print(f"{'teacher_id':<15}{'First Name':<15}{'Last Name':<15}{'Class':<10}{'Date of Birth'}\t{'Address'}\t{'Contact No'}")
    for teacher in teachers:
        print(f"{teacher[0]:<15}{teacher[1]:<15}{teacher[2]:<15}{teacher[3]:<10}{teacher[4]}\t{teacher[5]}\t{teacher[6]}")

# Main program loop

while True:
    print("\n------------------WELCOME IN SCHOOL MANAGEMENT PANNEL------------------\n")
    print("1. Student Panel")
    print("2. Teacher Panel")
    print("3. Exit\n")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        while True:
            print("\n------------------WELCOME IN STUDENT PANNEL------------------\n")
            print("Enter 1 : To Regester Student ")
            print("Enter 2 : To Edit Detail Of Existing student  ")
            print("Enter 3 : To Delete Data of Existing Student  ")
            print("Enter 4 : To Show all Students Data  ")
            print("Enter 5 : To Exit\n")
            
            ch=int(input("Enter your Choice : "))
            if ch==1:
                register_student()
            elif ch==2:
                edit_student()
            elif ch==3:
                delete_student()
            elif ch==4:
                print("\nStudents Active :- \n")
                show_students(status="Active")
                print()
                print("\nStudents Left:-\n")
                show_students(status="Left")
                print("\n-------------------------------------------------------------------------\n")
            elif ch==5:
                break
            else:
                pass
        
    elif choice==2:
        while True:
            print(print("\n------------------WELCOME IN STUDENT PANNEL------------------\n"))
            print("Enter 1 : To Regester new Teacher : ")
            print("Enter 2 : To Edit Detail of Existing Teacher")
            print("Enter 3 : To Deleting existing data of Teacher")
            print("Enter 4 : To Show All Data Of Teachers")
            print("Enter 5 : To Exit\n")
            #query
            ch=int(input("Enter your Choice : "))
            if ch==1:
                register_teacher()
            elif ch==2:
                edit_teacher()
            elif ch==3:
                delete_teacher()
            elif ch==4:
                print("\nTeacher Active :- \n")
                show_teachers(status="Active")
                print()
                print("\nTeacher Left:-\n")
                show_teachers(status="Left")
                print("\n-------------------------------------------------------------------------\n")
            elif ch==5:
                break
            else:
                pass
    elif choice==3:
        print("\nThanks For Using this Program\n")
        print("See you soon...\n")
        break
    
    else:
        print("\nInvalid Choice\n")
        



# Close MySQL connection
db.close()
