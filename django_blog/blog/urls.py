from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CreatePost,DeletePost,ListPost,PostDetail,UpdatePost

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('posts/', ListPost.as_view(), name='post_list'),                
    path('post/new/', CreatePost.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='post_delete'),
]