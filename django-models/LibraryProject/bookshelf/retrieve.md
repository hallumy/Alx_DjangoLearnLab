# Retrieve and display all attributes of the book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Output:
# 1984 George Orwell 1949

