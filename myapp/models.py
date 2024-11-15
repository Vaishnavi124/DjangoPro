from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    image=models.ImageField(upload_to='')
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=10000)
    author=models.CharField(max_length=30)
    price=models.IntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

# class Cart(models.Model):
#     session_id = models.CharField(max_length=255, unique=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
# here session is created instead of authentication or authorization of the user, instead of  associating a cart with a User, 
# we could associate the cart with a session ID that is automatically created when a user visits the site, for that we need to import Session. 

# Here session_id is used to store the session key for the cart, which is unique for each visitor

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2)