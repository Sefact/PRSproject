from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    division = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200)
    call = models.CharField(max_length=100)
    park = models.CharField(max_length=50)
    hours = models.CharField(max_length=50)
    price = models.TextField(max_length=200)
    image_one = models.ImageField(upload_to="images/like/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/like/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/like/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/like/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/like/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)

    def __str__(self):
        return "text : "+self.text

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])

# Create your models here.
