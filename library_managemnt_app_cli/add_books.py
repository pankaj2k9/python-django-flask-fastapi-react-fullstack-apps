from save_all_books import save_all_books
import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    while True:
        try:
            year = int(input("Enter Publishing Year Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")
    
    while True:
        try:
            price = int(input("Enter Book Price: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid price.")
    
    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")

    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt
    }

    all_books.append(book)
    save_all_books(all_books)
    print("Books Added Successfully")
    return all_books
