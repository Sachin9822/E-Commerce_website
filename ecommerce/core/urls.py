from django.urls import path
from .views import *

app_name = 'ecommerce'
urlpatterns = [
            path('home/',HomeView.as_view(),name='Item-list'),
            path('seller/',SellerView.as_view(),name='Seller'),
            path('checkout/',checkout,name='Checkout'),
            path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
            path('product/<slug>/',ItemDetailView.as_view(),name="product"),
            path('add-to-cart/<slug>/',add_to_cart,name="add-to-cart"),
            path('remove-from-cart/<slug>/',remove_from_cart,name="remove-from-cart")
        ] 

