from django.db import models

# Author Model
# Represents a writer in the system.
# Each Author can be linked to multiple Book objects
# (this is a ONE-to-MANY relationship: one author → many books).

class Author(models.Model):
     """
    Represents a book author.
    Fields:
        - name: Author's name (string).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book Model
# Represents a published book in the system.
# Each Book must be linked to exactly one Author (via ForeignKey).

class Book(models.Model):
    """
    Represents a book written by an author.
    Fields:
        - title: Title of the book (string).
        - publication_year: Year of publication (integer).
        - author: ForeignKey to Author (many books per author).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

     # Link to the Author who wrote the book.
     # related_name="books" → allows us to access an author's books via author.books.all()
     # on_delete=models.CASCADE → if the author is deleted, their books will be deleted too.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        """
        String representation of the Book object.
        This will be used in Django Admin and anywhere else the object
        is converted to a string.
        """ 
        return f"{self.title} ({self.publication_year})"

