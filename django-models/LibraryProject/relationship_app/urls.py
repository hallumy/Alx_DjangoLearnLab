from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.list_books, name='list_books'),                 # Function-based view
    path('', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
