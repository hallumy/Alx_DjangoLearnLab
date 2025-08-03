# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Output:book object (1)
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

