from django.shortcuts import render
from django.http import HttpResponse
from relationship_app.models import book
# Create your views here.

def list_books(request):
    """Function-based view that returns all books and their authors as plain text"""
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
    
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.select_related('author').all()
        return context

