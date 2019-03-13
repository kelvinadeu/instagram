from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile,Image,Comment,Location

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image_path','username','image_description',)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('profile_pic','bio',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
