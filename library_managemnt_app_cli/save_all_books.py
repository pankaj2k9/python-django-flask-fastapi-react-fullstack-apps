import json

def save_all_books(all_books):
    with open("all_books.json", "w") as fp:
        json.dump(all_books, fp, indent=4)
