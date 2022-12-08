from django.conf import settings
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

class Items(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(choices=CAT_CHOICES,max_length=2)
    label = models.CharField(choices=LABLE_CHOICES,max_length=1)
    slug = models.SlugField()
    description = models.TextField()

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

class Orderitems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    pass

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(Orderitems)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    pass
