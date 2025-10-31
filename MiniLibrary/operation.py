

# Data Structures
books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Science", "Romance", "History", "Technology")

# Function to Add Book
def add_book(isbn, title, author, genre, copies):
    """Add a new book to the library."""
    if genre not in genres:
        return f"Invalid genre. Available genres: {genres}"
    if isbn in books:
        return "Book already exists."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "copies": copies
    }
    return f"Book '{title}' added successfully!"

#Function to Display All Books
def view_books():
    """Display all books in the library."""
    if not books:
        return "No books in the library."
    output = "=== Library Books ===\n"
    for isbn, info in books.items():
        output += f"ISBN: {isbn} | {info['title']} by {info['author']} | Genre: {info['genre']} | Copies: {info['copies']}\n"
    return output

#Function to Register Member
def register_member(member_id, name, email):
    """Register a new library member."""
    for m in members:
        if m["member_id"] == member_id:
            return "Member ID already exists."
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return f"Member '{name}' registered successfully!"

#Function to View Members
def view_members():
    """Display all library members."""
    if not members:
        return "No members registered."
    output = "=== Registered Members ===\n"
    for m in members:
        output += f"ID: {m['member_id']} | Name: {m['name']} | Email: {m['email']} | Borrowed: {m['borrowed_books']}\n"
    return output

#Function to Borrow Book
def borrow_book(member_id, isbn):
    """Allow a member to borrow a book if available."""
    if isbn not in books:
        return "Book not found."
    if books[isbn]["copies"] <= 0:
        return "No copies available."
    for m in members:
        if m["member_id"] == member_id:
            m["borrowed_books"].append(isbn)
            books[isbn]["copies"] -= 1
            return f"Book '{books[isbn]['title']}' borrowed by {m['name']}."
    return "Member not found."

#Function to Return Book
def return_book(member_id, isbn):
    """Allow a member to return a borrowed book."""
    for m in members:
        if m["member_id"] == member_id:
            if isbn in m["borrowed_books"]:
                m["borrowed_books"].remove(isbn)
                books[isbn]["copies"] += 1
                return f"Book '{books[isbn]['title']}' returned by {m['name']}."
            else:
                return "This member did not borrow that book."
    return "Member not found."