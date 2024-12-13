import add_books
import view_all_books
import update_books
import delete_books
import restore_books
import lend_book
import return_book
import load_lend_records

all_books = restore_books.restore_all_books([])
lend_records = load_lend_records.load_lend_records()

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend a Book")
    print("6. Return a Book")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = update_books.update_books(all_books)
    elif menu == "4":
        all_books = delete_books.delete_books(all_books)
    elif menu == "5":
        all_books, lend_records = lend_book.lend_book(all_books, lend_records)
    elif menu == "6":
        all_books, lend_records = return_book.return_book(all_books, lend_records)
    else:
        print("Choose a valid number")
