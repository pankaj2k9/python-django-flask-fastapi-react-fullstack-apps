from save_all_books import save_all_books
import json
from datetime import datetime, timedelta

def lend_book(all_books, lend_records):
    borrower_name = input("Enter Borrower's Name: ")
    borrower_phone = input("Enter Borrower's Phone: ")
    book_title = input("Enter Book Title to Lend: ")

    # Search for the book in the library
    for book in all_books:
        if book["title"] == book_title:
            if book["quantity"] > 0:
                return_due_date = datetime.now() + timedelta(days=14)
                return_due_date_str = return_due_date.strftime("%d-%m-%Y %H:%M:%S")

                # Record the lending details
                lend_record = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book_title,
                    "return_due_date": return_due_date_str
                }
                lend_records.append(lend_record)

                # Decrease the book's quantity
                book["quantity"] -= 1

                # Save the updated data
                save_all_books(all_books)
                with open("lend_records.json", "w") as fp:
                    json.dump(lend_records, fp, indent=4)

                print(f"Book '{book_title}' lent successfully to {borrower_name}. Return by {return_due_date_str}.")
                return all_books, lend_records
            else:
                print("Not enough books are available to lend.")
                return all_books, lend_records

    print("Book not found in the library.")
    return all_books, lend_records
