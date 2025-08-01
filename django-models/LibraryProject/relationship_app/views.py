from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def list_books(request):
    """Function-based view that returns all books and their authors as plain text"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
    
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.select_related('author').all()
        return context

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Built-in LogoutView
class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Custom register view using built-in form
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return hasattr(user, 'profile') and user.profile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return hasattr(user, 'profile') and user.profile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')