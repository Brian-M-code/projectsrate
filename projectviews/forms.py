from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from projectviews.models import Projects,Profile
from django.contrib.auth.forms import UserCreationForm

class ProjectUploadForm(forms.ModelForm):
    
    class Meta:
        model = Projects
        fields = ('image', 'description', 'title', 'link', 'author')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('design', 'usability', 'content','creativity')