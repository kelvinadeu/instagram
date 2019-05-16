from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import *
from .forms import *
# Create your views here.
def login(request):
    return render(request,'registration/login.html')
@login_required(login_url='/accounts/login/')
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
    # print(comment)
    image_id = request.POST.get('image_id')
    image = get_object_or_404(Image ,id=image_id)
    user=get_object_or_404(User, id=request.user.id)
    # comments = Comments.objects.create(image_id=image, comment=comment,user_id=user)
    return redirect ('home.html')

    comments=Comment.objects.all()
    likes = Like.objects.all()
    for post in posts:
        num_likes=0
        for like in likes:
            if post.id == like.post.id:
                num_likes +=1
        post.likes = num_likes
        post.save()

        if request.method == 'POST' and 'liker' in request.POST:
            post_id = request.POST.get("liker")
            likeform = LikeForm(request.POST)
            if likeform.is_valid():
                post_id = int(request.POST.get("liker"))
                post = Post.objects.get(id = post_id)
                like = likeform.save(commit=False)
                like.username = request.user
                like.post = post
                like.control = str(like.username.id)+"-"+str(like.post.id)
                like.save()
                print("like saved")

        return redirect("timeline")
    else:
        likeform = LikeForm()
    if request.method == 'POST' and 'unliker' in request.POST:
                post_id = request.POST.get("unliker")
                post = Post.objects.get(pk=post_id)
                control = str(request.user.id)+"-"+str(post.id)
                like_delete = Like.objects.get(control=control)
                like_delete.delete()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = int(request.POST.get("idpost"))
            post = Post.objects.get(id = post_id)
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = post
            comment.save()
        return redirect('timeline')

    else:
        form = CommentForm()

    posts= Post.objects.all().order_by("-id")
    likes = Like.objects.all()
    likez = Like.objects.values_list('control', flat=True)
    likez =list(likez)

    return render(request,'timeline.html',{"posts":posts,"profiles":profiles,"current_user":current_user,"comments":comments,"form":form, "likeform":likeform, "likes":likes,"likez":likez,})





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
