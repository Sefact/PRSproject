from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Cafe(models.Model):
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
    image_one = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:200]

class Art(models.Model):
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
    image_one = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:200]

class Food(models.Model):
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
    image_one = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:200]

class Theater(models.Model):
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
    image_one = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:200]

class Escape(models.Model):
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
    image_one = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:200]

class Travle(models.Model):
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
    image_one = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_two = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_three = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_four = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    image_five = models.ImageField(upload_to="images/tag/%Y/%m/%d", blank=True, null=True)
    maps = models.ImageField(upload_to="images/maps/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:200]