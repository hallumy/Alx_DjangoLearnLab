from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.list_books, name='list_books'),                 # Function-based view
    path('', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('login/', LoginView.as_view(), template_name='login'),
    path('logout/', LogoutView.as_view(), template_name='logout'),
    path('register/', views.register_view, template_name='register'),
]
