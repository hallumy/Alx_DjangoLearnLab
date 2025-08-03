from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register_view, admin_view, librarian_view, member_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.list_books, name='list_books'),                 # Function-based view
    path('', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
