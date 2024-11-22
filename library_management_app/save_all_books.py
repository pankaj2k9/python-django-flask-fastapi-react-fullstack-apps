def save_all_books(all_books):
    with open("all_books.csv", "w") as file:
        for book in all_books:
            line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['price']}, {book['quantity']}\n"
            file.write(line)
