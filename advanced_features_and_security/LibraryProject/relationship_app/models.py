from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractUser
from django.conf import settings
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        ]
    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user.username}"
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True)
    profile_photo = models.ImageField(upload_to='profile_images/', blank=True)
    
    def __str__(self):
        return self.username

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with a given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of 
        birth and password
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user