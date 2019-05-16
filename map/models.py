from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'pics/')
    followers = models.ManyToManyField('Profile',related_name='followers_profile',blank=True)
    following = models.ManyToManyField('Profile', related_name='following_profile',blank=True)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=100,blank=True)

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
           return self.following.count
        else:
           return 0

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def save_user(self):
        self.save()

    @classmethod
    def search_user(cls,username):
        searched_user = User.objects.get(username = username)
        return searched_user

    def __str__(self):
        return self.user.username

class  Image(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,)
    image_path = models.ImageField(upload_to = 'photos/')
    image_description = models.CharField(max_length=100,blank=True)
    post = models.TextField()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.image_description

class Location(models.Model):

    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_Location(self):
        self.save()

class Comment(models.Model):
    post = models.ForeignKey('Image',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

class Like(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Image,on_delete=models.CASCADE)
    control = models.CharField(max_length=50,unique=True, null=True)

    def __str__(self):
        return self.control

    def save_like(self):
        self.save()
