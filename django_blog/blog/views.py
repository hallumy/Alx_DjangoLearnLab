from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")
    
    return render(request, "blog/profile.html", {"user": request.user})
    
def home(request):
    return render(request, "blog/home.html")

def posts(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {"posts":posts})

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'published_date', 'author']
    template_name = 'blog/Post_form.html'
    
    def form_valid(self, form):
        # Automatically set the author as the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ListPost(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    
class PostDetail(DetailView):
    model = Post

class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePost(DeleteView):
    model = Post 
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")


