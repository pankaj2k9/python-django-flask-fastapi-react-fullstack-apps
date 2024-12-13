from save_all_books import save_all_books
import json

def return_book(all_books, lend_records):
    borrower_name = input("Enter Borrower's Name: ")
    book_title = input("Enter Book Title to Return: ")

    # Search for the lending record
    for record in lend_records:
        if record["borrower_name"] == borrower_name and record["book_title"] == book_title:
            lend_records.remove(record)

            # Increase the book's quantity
            for book in all_books:
                if book["title"] == book_title:
                    book["quantity"] += 1

            # Save the updated data
            save_all_books(all_books)
            with open("lend_records.json", "w") as fp:
                json.dump(lend_records, fp, indent=4)

            print(f"Book '{book_title}' returned successfully by {borrower_name}.")
            return all_books, lend_records

    print("No matching lend record found.")
    return all_books, lend_records
