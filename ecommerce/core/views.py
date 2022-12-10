from django.contrib import messages
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
    order_item , created = Orderitems.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
    order_qs = Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check is the item is already in the cart
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            order_item.save()
            messages.info(request,"This item quantity was updated")
        else:
            messages.info(request,"This item was added in cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"The order item was added")

    return redirect("core:product",slug=slug)

def remove_from_cart(request,slug):
    item = get_object_or_404(Items,slug=slug)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = Orderitems.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                    )[0]
            order.items.remove(order_item)
            messages.info(request,"item was removed from your cart")
            return redirect("core:product",slug=slug)
        else:
            # the order item does not exists
            messages.info(request,"item is does not exist in the cart")
            return redirect("core:product",slug=slug)
    else:
        # tell user that he doesnt have a product
        messages.info(request,"User doesnt have an order")
        return redirect("core:product",slug=slug)

def checkout(request):
    context = {
            'orders_items': Orderitems.objects.all()
        }
    return render(request,"checkout-page.html",context)

def product_page(request):
    return render(request,"product-page.html")
