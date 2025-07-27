import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author."""
    books = Book.objects.filter(author__name=author_name)
    return books

def list_books_in_library(library_name):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # reverse OneToOneField
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
