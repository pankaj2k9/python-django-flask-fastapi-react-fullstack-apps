import add_books
import view_all_books
import update_books
import remove_books

all_books = []

while True:
    print(f"\nWelcome to our Library Management System! Please select below menu ID")
    print("Menu ID= 1. Add a New Book.")
    print("Menu ID= 2. Update your Book.")
    print("Menu ID= 3. Remove a Select Book.")
    print("Menu ID= 4. View ALL Books.")
    print("Menu ID= 5. Exit.")

    menu = input(f"\nSelect any Number: ")
    
    if menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        all_books = update_books.update_books(all_books)
    elif menu == "3":
        all_books = remove_books.remove_books(all_books)
    elif menu == "4":
        view_all_books.view_all_books(all_books)
    elif menu == "5":
        print(f"\nThanks for using our Library Management System!")
        break
    else:
        print("Please Select a Valid Number")
