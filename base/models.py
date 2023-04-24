from django.db import models
from django.contrib.auth.models import User
import os
import random

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	Profile_filename = random.randint(1, 2541781232)
	name, ext = get_filename_ext(filename)
	final_filename = '{Profile_filename}{ext}'.format(Profile_filename=Profile_filename, ext=ext)
	return "img/{Profile_filename}/{final_filename}".format(Profile_filename=Profile_filename, final_filename=final_filename)
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    download = models.FileField(null=True, blank=True)
    watch = models.CharField(max_length=200, null=True, blank=True)
    isBasic = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    preorderdate = models.DateField(auto_now_add=False, null=True, blank=True)
    numofPreorder = models.IntegerField(null=True, blank=True, default=0)
    isBought = models.BooleanField(default=True)
    

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name



    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    download = models.FileField(null=True, blank=True)
    isBasic = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    preorderdate = models.DateField(auto_now_add=False, null=True, blank=True)
    isBought = models.BooleanField(default=False)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    isBasic = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    download = models.CharField(max_length=200, null=True, blank=True)
    preorderdate = models.DateField(auto_now_add=False, null=True, blank=True)
    isBought = models.BooleanField(default=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_friend = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False, default=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
   

class Profile(models.Model):

    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('gaming', 'Gaming'),
        ('politics', 'Politics'),
        # add more choices as needed
    ]
    
    _id = models.AutoField(primary_key=True, editable=False)
    isVerified = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    
    headline = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)


    def __str__(self):
        return str(self.headline)
    
class HeartList(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='hearts_given')
    userReceiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='hearts_received')
    userOwner= models.CharField(max_length=200, null=True, blank=True)
    userHeart= models.CharField(max_length=200, null=True, blank=True)
    resume = models.FileField(null=True, blank=True) # Add this line to create the resume field
    letter = models.CharField(max_length=200, null=True, blank=True)
    # whotoheart = models.CharField(max_length=200, null=True, blank=True)
    isHeart = models.BooleanField(default=False)
    canMessage = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

  

    
class Sport(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    createdAt = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.headline)
    
class Gaming(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    createdAt = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.headline)
    
class Review(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)

    # gaming = models.ForeignKey(Gaming, on_delete=models.SET_NULL, null=True)

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)
    
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='playlists/', blank=True, null=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

