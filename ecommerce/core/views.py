from django.utils import timezone
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import *


# Create your views here.

class HomeView(ListView):
    model = Items 
    template_name="home-page.html"

class ItemDetailView(DetailView):
    model= Items
    template_name="product-page.html"

def add_to_cart(request,slug):
    item = get_object_or_404(Items,slug=slug) 
    order_item = Orderitems.objects.get_or_create(item=item)
    order_qs = Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check is the item is already in the cart
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product",slug=slug)


def checkout(request):
    context = {
            'orders_items': Orderitems.objects.all()
        }
    return render(request,"checkout-page.html",context)

def product_page(request):
    return render(request,"product-page.html")
