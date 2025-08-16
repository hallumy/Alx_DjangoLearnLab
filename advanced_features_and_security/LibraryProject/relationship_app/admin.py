from django.contrib import admin
from .models import Author, Book, Library, Librarian
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the list view
    list_display = ("email", "username", "date_of_birth", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser")

    # Fields shown when viewing/editing a user
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields shown when creating a user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "date_of_birth", "profile_photo", "password1", "password2", "role", "is_staff", "is_superuser"),
        }),
    )

    search_fields = ("email", "username")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

