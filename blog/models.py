from django.db import models
from django.contrib.auth.models import User

class Author (models.Model):
    firstName = models.CharField(max_length=60 , blank=True)
    lastName = models.CharField (max_length=60 , blank=True)
    email = models.EmailField(blank=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Use User instead of Author
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


