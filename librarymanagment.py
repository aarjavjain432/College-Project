library_books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'is_loaned': False},
    {'title': '1984', 'author': 'George Orwell', 'is_loaned': True},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'is_loaned': False},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'is_loaned': False}
]

def display_menu():
    """Prints the main menu options to the console."""
    print("\n==============================")
    print("  Simple Library Manager Menu")
    print("==============================")
    print("1. Display All Books")
    print("2. Add a New Book")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit")
    print("==============================")

def display_books(books):
    """Prints a formatted list of all books in the library."""
    if not books:
        print("\n[INFO] The library is currently empty.")
        return

    print("\n--- Current Library Collection ---")
    for i, book in enumerate(books):
        status = " (Loaned)" if book['is_loaned'] else " (Available)"
        print(f"[{i+1}] Title: {book['title']}, Author: {book['author']}{status}")
    print("-" * 34)

def add_book():
    """Prompts the user for book details and adds a new book to the list."""
    print("\n--- Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    if not title or not author:
        print("\n[ERROR] Both title and author must be provided. Book not added.")
        return
    new_book = {
        'title': title,
        'author': author,
        'is_loaned': False
    }
    library_books.append(new_book)
    print(f"\n[SUCCESS] '{title}' by {author} has been added to the library.")

def find_book_by_title(title_to_find):
    """Searches the library list for a book by title (case-insensitive)."""
    matches = [book for book in library_books if book['title'].lower() == title_to_find.lower()]
    return matches[0] if matches else None

def borrow_book():
    """Handles the borrowing process for an available book."""
    print("\n--- Borrow a Book ---")
    title_to_borrow = input("Enter the title of the book you want to borrow: ").strip()
    book = find_book_by_title(title_to_borrow)

    if book:
        if not book['is_loaned']:
            book['is_loaned'] = True
            print(f"\n[SUCCESS] You have successfully borrowed '{book['title']}'. Enjoy!")
        else:
            print(f"\n[INFO] '{book['title']}' is currently loaned out. Try again later.")
    else:
        print(f"\n[ERROR] Book with title '{title_to_borrow}' not found in the library.")

def return_book():
    """Handles the returning process for a loaned book."""
    print("\n--- Return a Book ---")
    title_to_return = input("Enter the title of the book you are returning: ").strip()

    book = find_book_by_title(title_to_return)

    if book:
        if book['is_loaned']:
            book['is_loaned'] = False
            print(f"\n[SUCCESS] Thank you for returning '{book['title']}'.")
        else:
            print(f"\n[INFO] '{book['title']}' was already available in the library.")
    else:
        print(f"\n[ERROR] Book with title '{title_to_return}' not found in the system.")

def main():
    """The main function that runs the library system loop."""
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                display_books(library_books)
            elif choice == '2':
                add_book()
            elif choice == '3':
                borrow_book()
            elif choice == '4':
                return_book()
            elif choice == '5':
                print("\n[INFO] Thank you for using the Simple Library Manager. Goodbye!")
                break 
            else:
                print("\n[ERROR] Invalid choice. Please enter a number between 1 and 5.")
                
        except Exception as e:
            print(f"\n[CRITICAL ERROR] An unexpected error occurred: {e}")
            print("Please try again.")
            
if __name__ == "__main__":
    main()