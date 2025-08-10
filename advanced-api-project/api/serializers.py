from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of the Book model

    def validate_publication_year(self, value):
        """Ensure publication_year is not in the future."""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # books → refers to the related_name in Book.author
    # many=True → because one author can have many books
    # read_only=True → prevents creating books through AuthorSerializer directly
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

"""
The relationship between Author and Book is defined in the Book model
via a ForeignKey field pointing to Author.

In the serializers:
- BookSerializer handles a single book and includes its 'author' field.
- AuthorSerializer includes a nested 'books' field that uses BookSerializer.
  This uses the 'related_name="books"' from the Book model to fetch all books
  for a given author.
"""
