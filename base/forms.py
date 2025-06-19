from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Course

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','avatar','password1','password2']

class CourseForm(ModelForm):
    
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['creator','participants']
