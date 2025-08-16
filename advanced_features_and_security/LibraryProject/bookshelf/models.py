from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, BaseUserManager, AbstractUser
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0)

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

class CustomUserManager(BaseUserManager):
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