import mysql.connector

# Establish a MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library_db"
)

# Create a cursor object
cursor = conn.cursor()

def public_portal():
    while True:
        print("Public Portal:")
        print("1. Display Books")
        print("2. Search Books")
        print("3. Borrow Books")
        print("4. Return Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            borrow_books()
        elif choice == "4":
            return_books()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def admin_portal():
    while True:
        print("Admin Portal:")
        print("1. No. of Users")
        print("2. Books Borrowed")
        print("3. Books Returned")
        print("4. Add New Users")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            count_users()
        elif choice == "2":
            count_borrowed_books()
        elif choice == "3":
            count_returned_books()
        elif choice == "4":
            add_new_user()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def display_books():
    # Retrieve and display all books from the database
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available Copies: {book[3]}")

def search_books():
    title = input("Enter the title of the book to search: ")
    # Search for books with the given title in the database
    cursor.execute("SELECT * FROM books WHERE title = %s", (title,))
    books = cursor.fetchall()
    if books:
        for book in books:
            print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available Copies: {book[3]}")
    else:
        print("Book not found.")

def borrow_books():
    user_id = input("Enter your user ID: ")
    book_id = input("Enter the book ID you want to borrow: ")
    # Check if the book is available
    cursor.execute("SELECT available_copies FROM books WHERE book_id = %s", (book_id,))
    available_copies = cursor.fetchone()[0]
    if available_copies > 0:
        # Borrow the book
        cursor.execute("INSERT INTO borrowed_books (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
        cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE book_id = %s", (book_id,))
        conn.commit()
        print("Book successfully borrowed.")
    else:
        print("Sorry, the book is not available for borrowing.")

def return_books():
    user_id = input("Enter your user ID: ")
    book_id = input("Enter the book ID you want to return: ")
    # Check if the user has borrowed the book
    cursor.execute("SELECT * FROM borrowed_books WHERE user_id = %s AND book_id = %s", (user_id, book_id))
    if cursor.fetchone():
        # Return the book
        cursor.execute("DELETE FROM borrowed_books WHERE user_id = %s AND book_id = %s", (user_id, book_id))
        cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id = %s", (book_id,))
        conn.commit()
        print("Book successfully returned.")
    else:
        print("You have not borrowed this book.")

def count_users():
    # Retrieve and display the number of users from the database
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"Total number of users: {count}")

def count_borrowed_books():
    # Retrieve and display the number of books borrowed from the database
    cursor.execute("SELECT COUNT(*) FROM borrowed_books")
    count = cursor.fetchone()[0]
    print(f"Total number of books borrowed: {count}")

def count_returned_books():
    # Retrieve and display the number of books returned from the database
    cursor.execute("SELECT COUNT(*) FROM borrowed_books")
    count_borrowed = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM returned_books")
    count_returned = cursor.fetchone()[0]
    print(f"Total number of books returned: {count_returned}/{count_borrowed}")

def add_new_user():
    name = input("Enter the name of the new user: ")
    # Add the new user to the database
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    print("New user added successfully.")

if __name__ == "__main":
    while True:
        print("Library Management System:")
        print("1. Public Portal")
        print("2. Admin Portal")
        print("3. Exit")
        portal_choice = input("Enter your choice: ")

        if portal_choice == "1":
            public_portal()
        elif portal_choice == "2":
            admin_portal()
        elif portal_choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Close the cursor and connection when done
cursor.close()
conn.close()
