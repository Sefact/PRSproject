from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Blike(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    division = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200)
    call = models.CharField(max_length=100)
    park = models.CharField(max_length=50)
    hours = models.CharField(max_length=50)
    price = models.TextField(max_length=200)
    context = models.TextField(max_length=500, null=True, blank=True)
    image_one = models.ImageField(upload_to="images/blog/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/blog/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/blog/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/blog/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/blog/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:200]

class Beditor(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    division = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200)
    call = models.CharField(max_length=100)
    park = models.CharField(max_length=50)
    hours = models.CharField(max_length=50)
    price = models.TextField(max_length=200)
    context = models.TextField(max_length=500, null=True, blank=True)
    image_one = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LikeComment(models.Model):
    blike = models.ForeignKey(Blike, on_delete=models.CASCADE, related_name='like_comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='like_comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return (self.author.username if self.author else "무명")+ "의 댓글"