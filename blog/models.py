from django.db import models
from django.contrib.auth.models import User

class Author (models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField (max_length=60)
    email = models.EmailField()

class Post(models.Model):  
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


