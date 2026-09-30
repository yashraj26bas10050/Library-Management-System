"""Student Library Management System - terminal based Python project."""
import json
import os

DATA_FILE = os.path.join("data", "books.json")


def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            books = json.load(file)
        return books if isinstance(books, list) else []
    except (json.JSONDecodeError, OSError):
        print("\nCould not read the saved library data.")
        return []


def save_books(books):
    os.makedirs("data", exist_ok=True)
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)
        return True
    except OSError:
        print("\nCould not save the library data.")
        return False


def get_required_input(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def find_book(books, book_id):
    for book in books:
        if book["book_id"].lower() == book_id.lower():
            return book
    return None


def print_books(books):
    if not books:
        print("\nNo books to show.")
        return
    print("\n" + "-" * 78)
    print(f"{'ID':<12}{'TITLE':<30}{'AUTHOR':<22}{'STATUS':<14}")
    print("-" * 78)
    for book in books:
        print(f"{book['book_id']:<12}{book['title'][:28]:<30}"
              f"{book['author'][:20]:<22}{book['status']:<14}")
    print("-" * 78)


def add_book(books):
    print("\n--- Add a Book ---")
    while True:
        book_id = get_required_input("Book ID: ")
        if find_book(books, book_id):
            print("That Book ID is already being used.")
        else:
            break
    title = get_required_input("Book title: ")
    author = get_required_input("Author: ")
    books.append({"book_id": book_id, "title": title,
                  "author": author, "status": "Available"})
    if save_books(books):
        print(f"\n'{title}' has been added to the library.")


def view_books(books):
    print("\n--- All Books ---")
    print_books(books)


def search_books(books):
    print("\n--- Search Books ---")
    term = get_required_input("Enter a Book ID, title, or author: ").lower()
    matches = [book for book in books if term in book["book_id"].lower()
               or term in book["title"].lower()
               or term in book["author"].lower()]
    if matches:
        print(f"\nFound {len(matches)} matching book(s):")
        print_books(matches)
    else:
        print("\nNo books matched your search.")


def borrow_book(books):
    print("\n--- Borrow a Book ---")
    book = find_book(books, get_required_input("Book ID: "))
    if book is None:
        print("That Book ID could not be found.")
        return
    if book["status"] == "Borrowed":
        print("That book is already borrowed.")
        return
    book["status"] = "Borrowed"
    if save_books(books):
        print(f"\nYou have borrowed '{book['title']}'.")


def return_book(books):
    print("\n--- Return a Book ---")
    book = find_book(books, get_required_input("Book ID: "))
    if book is None:
        print("That Book ID could not be found.")
        return
    if book["status"] == "Available":
        print("That book is already marked as available.")
        return
    book["status"] = "Available"
    if save_books(books):
        print(f"\n'{book['title']}' has been returned.")


def remove_book(books):
    print("\n--- Remove a Book ---")
    book = find_book(books, get_required_input("Book ID: "))
    if book is None:
        print("That Book ID could not be found.")
        return
    if book["status"] == "Borrowed":
        print("This book is borrowed. Return it before removing it.")
        return
    books.remove(book)
    if save_books(books):
        print(f"\n'{book['title']}' has been removed.")


def show_library_status(books):
    total = len(books)
    borrowed = sum(1 for book in books if book["status"] == "Borrowed")
    print("\n--- Library Status ---")
    print(f"Total books     : {total}")
    print(f"Available books : {total - borrowed}")
    print(f"Borrowed books  : {borrowed}")


def show_menu():
    print("\n" + "=" * 44)
    print("       STUDENT LIBRARY MANAGEMENT")
    print("=" * 44)
    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Remove a book")
    print("7. Show library status")
    print("8. Exit")
    print("=" * 44)


def main():
    books = load_books()
    print("\nWelcome to the Student Library Management System.")
    print("Keep track of your books directly from the terminal.")
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            remove_book(books)
        elif choice == "7":
            show_library_status(books)
        elif choice == "8":
            print("\nThanks for using the Student Library Management System.")
            break
        else:
            print("\nThat is not a valid option. Please choose 1 to 8.")


if __name__ == "__main__":
    main()
