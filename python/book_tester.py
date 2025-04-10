from book import Book

# Create list to store book objects.
books = []

# Open file.
with open("books.txt") as file:
    for book in file:
        # Split at commas
        info = book.strip().split(",")
        # Create object
        book = Book(info[0], info[1], info[2])
        books.append(book)
        print(book)

# Calling methods on first book.
print(books[0].get_title())
print(books[0].get_author())
print(books[0].get_genre())
print(books[0].is_checked_out())

# Checking out and returning the first book.
books[0].check_out()
print(books[0])
books[0].return_book()
print(books[0])
