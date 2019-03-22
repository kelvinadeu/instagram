from django.test import TestCase
from .models import Comments, Image, Profile
from django.core.files.uploadedfile import SimpleUploadedFile


class Comment(TestCase):

    def setUp(self):

        self.profile = User.objects.create(username="profile")
        self.picture = Image.objects.create(image='image1', user=self.loise)
        self.comment = Review.objects.create(comment = 'so ugly')

        self.test_review = Review.objects.create(user=self.loise, image=self.image1, comment='so ugly')
        self.test_review.save()

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.test_reviews, Review))
