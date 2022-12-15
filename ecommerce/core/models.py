from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.views.generic import ListView,DetailView
from django.db import models

# Create your models here.
CAT_CHOICES = (
        ('S','Shirt'),
        ('SW','Spots wear'),
        ('OW','Outwear')
    )

LABLE_CHOICES= (
        ('P',"primary"),
        ('S',"secondary"),
        ('D',"danger"),
    )
STATUS_CHOICES= (
        ('NP',"Not Processed"),
        ('P',"Processing"),
        ('OD',"Out for Delivery"),
        ('D',"Delivered"),
    )

# user_group = User.objects.filter(groups_name='user') 
# user_group = user_group.user_set.all()
# seller_group = User.objects.filter(groups_name='seller') 
# seller_group = seller_group.user_set.all()
user_group = User
seller_group = User
class Items(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(choices=CAT_CHOICES,max_length=2)
    label = models.CharField(choices=LABLE_CHOICES,max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    
    user = models.ForeignKey(user_group,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',default=None) 

    def __str__(self):
        return self.title
    pass

    def get_absolute_url(self):
        return reverse("core:product",kwargs={
                'slug': self.slug
            })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart",kwargs={
                'slug': self.slug
            })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart",kwargs={
                'slug': self.slug
            })

class SellerOrders(models.Model):
    seller = models.ForeignKey(seller_group,on_delete=models.CASCADE)
    products = models.ManyToManyField(Items)


class Orderitems(models.Model):
    user = models.ForeignKey(user_group,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(choices=STATUS_CHOICES,max_length=2) 

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    pass

class Order(models.Model):
    user = models.ForeignKey(user_group,on_delete=models.CASCADE)
    items = models.ManyToManyField(Orderitems)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    pass

