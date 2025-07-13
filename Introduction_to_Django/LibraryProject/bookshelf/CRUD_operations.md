# Django Book Model - CRUD Operations via Shell

---

## Create

```python
from library.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output:
# <Book: 1984 by George Orwell (1949)>

## Retrieve

# Retrieve and display the book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output:
# 1984 George Orwell 1949

## Update

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

## Delete

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())
# Output:
# <QuerySet []>
