# Object-Oriented-Programming-
Mini Library System 

## Project Overview
This Mini Library Management System is a python-based console program that demonstrate the use of core data structures dictionaries lists tuples to manage library operation efficiently.

The system allows users to perform essential library function such as:
-Adding new books and members
-Searching and updating records
-Borrowing and returning books
-Deleting entries safely

This project follows the CRUD model
(Creat,read,update,delete) and includes unit tests to validate the core functionalities.

## 🧱 Data Structures Used

| Data Structure | Purpose | Example |
|----------------|----------|----------|
| Dictionary | Store book details with ISBN as key | { "978-001": {"title": "Python Basics", "author": "John Doe", "genre": "Fiction", "copies": 3} } |
| List | Maintain list of library members | [{"member_id": "M001", "name": "Alice", "email": "alice@gmail.com"}] |
| Tuple | Store fixed list of genres | ("Fiction", "Non-Fiction", "Sci-Fi", "Romance") |

---

## ⚙ System Files

| File | Description |
|------|--------------|
| operations.py | Contains all library CRUD functions |
| demo.py | Runs a demo of the system features |
| tests.py | Includes unit tests using assert |
| DesignRationale.pdf | Explains why each data structure was used |
| UML.png | Hand-drawn UML diagram showing structure |
| README.md | Project documentation and setup guide |

---

## 🚀 How to Run the Project

### Option 1: Run using Visual Studio Code (VSC)*
1. Open Visual Studio Code.  
2. Click File → Open Folder, then select your project folder.  
3. Ensure all files (operations.py, demo.py, tests.py, etc.) are in the same folder.  
4. In the terminal, run:

bash
python demo.py

You’ll see the main menu appear:

MINI LIBRARY MANAGEMENT SYSTEM 
1. Add Book
2. View Books
3. Borrow Book
4. Return Book
5. Exit


#Option 2: Run Tests
To verify your code works correctly, run:
python tests.py

#Key Features
Add, search, update, and delete books
Add and manage members
Borrow and return books with validation
Prevent duplicate IDs and ISBNs
Data organized using clean data structure

#Example Output
Added book: Python Basics by John Doe
Added member: Alice Johnson
Book borrowed successfully!
Book returned successfully!

#Developer
Name: Christian Julius Lalugba
Email: rectorchristianlalugba@gmail.com
Institution: Limkokwing University of Creative Technology – Sierra Leone
Year: 2025
If all assertions pass, no error message will appear.



