from django.shortcuts import render
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts, ordered by creation date
    return render(request, 'blog/home.html', {'posts': posts})

def post_update(reqeuest):
    pass

def post_delete(request):
    pass

def post_list(request):
    posts = Post.objects.all()  # Query the database
    return render(request, 'blog/post_list.html', {'post': posts}) 


def post_detail (request , pk):
    post = get_object_or_404(Post , pk = pk)
    return (render , 'blog/post_detail.html' , {'post' : post})


def post_create (request):
    if request.method== 'post':
        form = PostForm(request.post)
        if form.is_valid:
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return  redirect ('post_detail' , pk = post.pk)
    else:
        form = PostForm()
    return render  (request , 'blog/post_form.html' , {'form' : form})