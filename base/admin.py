from django.contrib import admin
from .models import Course, Posts, User

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Posts)