# demo.py

import operation as op

def menu():
    while True:
        print("\n=== MINI LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Register Member")
        print("4. View Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice (1,7): ")

        if choice == 1:
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            copies = int(input("Enter Number of Copies: "))
            print(op.add_book(isbn, title, author, genre, copies))

        elif choice == 2:
            print(op.view_books())

        elif choice == 3:
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            print(op.register_member(member_id, name, email))

        elif choice == 4:
            print(op.view_members())

        elif choice == 5:
            member_id = int(input("Enter Member ID: "))
            isbn = input("Enter ISBN: ")
            print(op.borrow_book(member_id, isbn))

        elif choice == 6:
            member_id = int(input("Enter Member ID: "))
            isbn = input("Enter ISBN: ")
            print(op.return_book(member_id, isbn))

        elif choice == 7:
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice! Please enter 1,7.")

if __name__ == "__main__":
    menu()