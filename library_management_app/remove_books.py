from view_all_books import view_all_books

def remove_books(all_books):
    view_all_books(all_books)
    book_index = int(input("Enter the number of the book to Remove: ")) - 1

    if 0 <= book_index < len(all_books):
        book = all_books.pop(book_index)
        print(f"\nYour Selected Book item '{book['title']}' has been Removed Successfully.")
    else:
        print("Invalid selection. Please try again.")

    return all_books
