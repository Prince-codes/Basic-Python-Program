import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="train_ticket_booking"
)
cursor = db.cursor()


def create_table():
    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(30),
            dob DATE,
            gender VARCHAR(2),
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    """)

def register():
    name=input("Enter Name : ")
    dob= input("Enter Date of Birth in 'yyyy/mm/dd' formate : ")
    gender=input("Enter Gender : ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Insert user details into the 'users' table
    cursor.execute("INSERT INTO users (name, dob, gender, username, password) VALUES (%s, %s, %s, %s, %s)", (name, dob, gender, username, password))
    db.commit()
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the user exists in the 'users' table
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        return True
    else:
        print("Login failed. Invalid credentials.")
        return False

def logout():
    print("Logout successful!")

def book_ticket():
    print("Ticket booked successfully!")

def cancel_ticket():
    print("Ticket canceled successfully!")

def main():
    create_table()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Book Ticket")
        print("5. Cancel Ticket")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            register()
            
        elif choice == 2:
            
            if login():
                
                while True:
                    
                    print("\n1. Book Ticket")
                    print("2. Cancel Ticket")
                    print("3. Logout")
                    
                    inner_choice = int(input("Enter your choice: "))
                    
                    if inner_choice == 1:
                        book_ticket()
                        
                    elif inner_choice == 2:
                        cancel_ticket()
                        
                    elif inner_choice == 3:
                        logout()
                        break
                    
                    else:
                        print("Invalid choice. Please try again.")
                        
        elif choice == 3:
            logout()
            
        elif choice == 4:
            book_ticket()
            
        elif choice == 5:
            cancel_ticket()
            
        elif choice == 6:
            print("Thank you for using the program!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
main()