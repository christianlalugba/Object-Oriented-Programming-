# tests.py

import operation as op

# Add sample books
print(op.add_book("B001", "Python Basics", "Guido Van Rossum", "Technology", 3))
print(op.add_book("B002", "Love in Lagos", "Chika Unigwe", "Romance", 2))

# Register sample members
print(op.register_member(1, "Christian Lalugba", "rectorchristianlalugba@gmail.com"))
print(op.register_member(2, "Mary Kamara", "mary@example.com"))

# View all books and members
print(op.view_books())
print(op.view_members())

# Borrow and return operations
print(op.borrow_book(1, "B001"))
print(op.return_book(1, "B001"))