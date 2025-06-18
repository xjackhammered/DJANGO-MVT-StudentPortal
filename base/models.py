from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, unique=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    type = models.CharField(null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

class Course(models.Model):
    creator = models.ManyToManyField(User)
    name = models.CharField(max_length=200)
    code = models.TextField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Posts(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    file = models.FileField(upload_to="post_files/", blank=True, null=True)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course