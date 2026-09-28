import json
import os

FILE_NAME = "library.json"


def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def add_book(books):
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available",
        "issued_to": ""
    }

    books.append(book)
    save_books(books)

    print("\nBook added successfully!")


def view_books(books):
    if not books:
        print("\nNo books available.")
        return

    print("\n" + "=" * 75)
    print("                         LIBRARY BOOKS")
    print("=" * 75)

    for book in books:
        print(f"ID       : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Status   : {book['status']}")

        if book["status"] == "Issued":
            print(f"Issued To: {book['issued_to']}")

        print("-" * 75)


def search_book(books):
    keyword = input("Enter book title or author to search: ").lower()

    found = False

    for book in books:
        if (keyword in book["title"].lower() or
                keyword in book["author"].lower()):

            print("\nBook Found!")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])

            found = True

    if not found:
        print("\nBook not found.")


def issue_book(books):
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                print("\nBook is already issued.")
                return

            student = input("Enter student name: ")

            book["status"] = "Issued"
            book["issued_to"] = student

            save_books(books)

            print("\nBook issued successfully!")
            return

    print("\nBook ID not found.")


def return_book(books):
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                print("\nThis book is already available.")
                return

            book["status"] = "Available"
            book["issued_to"] = ""

            save_books(books)

            print("\nBook returned successfully!")
            return

    print("\nBook ID not found.")


def remove_book(books):
    book_id = input("Enter Book ID to remove: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                print("\nCannot remove an issued book.")
                return

            books.remove(book)
            save_books(books)

            print("\nBook removed successfully!")
            return

    print("\nBook ID not found.")


def show_statistics(books):
    total = len(books)
    available = sum(1 for book in books if book["status"] == "Available")
    issued = sum(1 for book in books if book["status"] == "Issued")

    print("\n========== LIBRARY STATISTICS ==========")
    print("Total Books     :", total)
    print("Available Books :", available)
    print("Issued Books    :", issued)


def main():
    books = load_books()

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Library Statistics")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_book(books)

        elif choice == "4":
            issue_book(books)

        elif choice == "5":
            return_book(books)

        elif choice == "6":
            remove_book(books)

        elif choice == "7":
            show_statistics(books)

        elif choice == "8":
            print("\nThank you for using Library Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()