from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import *
from .forms import *
# Create your views here.
def home(request):
    count = User.objects.count()
    new = Image.objects.all()
    return render(request,'home.html',locals())


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    else:
        form = UserCreationForm()
    return render(request,'signup.html',{
        "form": form
    })

def save_comment(request):
    comment = request.POST.get('comment')
    print(comment)
    image_id = request.POST.get('image_id')
    image = get_object_or_404(Image, id=image_id)
    comments = Comments.objects.create(image_id=image,comment=comment)
    return redirect('home')

def profile_index(request):
    profiles = Profile.objects.all()
    forms=ProfileForm
    all_profile = Profile.objects.all()

    return render(request,'profile.html', locals())

def save_profile(request):
    all_profile = request.Post.get('profile')
    user_id = request.POST.get('user_id')

    all_profile = Profile.objects.create(user_id=user,profile=profile)
    return redirect('profile')
