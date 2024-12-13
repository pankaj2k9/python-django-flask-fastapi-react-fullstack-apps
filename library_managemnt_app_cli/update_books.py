from save_all_books import save_all_books
from datetime import datetime

def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book["title"] == search_book:
            title = input(f"Enter Book Title [{book['title']}]: ") or book["title"]
            author = input(f"Enter Author Name [{book['author']}]: ") or book["author"]
            while True:
                try:
                    year = input(f"Enter Publishing Year [{book['year']}]: ")
                    year = int(year) if year else book["year"]
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid year.")
            
            while True:
                try:
                    price = input(f"Enter Book Price [{book['price']}]: ")
                    price = int(price) if price else book["price"]
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price.")
            
            while True:
                try:
                    quantity = input(f"Enter Quantity Number [{book['quantity']}]: ")
                    quantity = int(quantity) if quantity else book["quantity"]
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookLastUpdatedAt"] = book_last_updated_at

            save_all_books(all_books)
            print("Book Updated Successfully")
            return all_books
    print("Book Not Found")
    return all_books
