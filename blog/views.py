from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, SignUpForm
from django.contrib.auth import login

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts, ordered by creation date
    return render(request, 'blog/home.html', {'posts': posts})

def post_update(request, pk):
    # Functionality for updating a post should be implemented here
    pass

def post_delete(request, pk):
    # Functionality for deleting a post should be implemented here
    pass

def post_list(request):
    posts = Post.objects.all()  # Query the database
    return render(request, 'blog/post_list.html', {'posts': posts})  # Fixed key to 'posts'

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})
