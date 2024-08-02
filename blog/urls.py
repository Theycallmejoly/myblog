# blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('my_posts/' , views.my_posts , name = 'my_posts'  ),
    path('', views.home, name='home'),  # Home page
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('post/<int:pk>/edit/', views.update_post, name='post_update'),
    path('post/<int:pk>/delete/', views.delete_post, name='post_delete'),
]
