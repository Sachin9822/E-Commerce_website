from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
            path('',HomeView.as_view(),name='Item-list'),
            path('checkout/',checkout,name='Checkout'),
            path('product/<slug>/',ItemDetailView.as_view(),name="product"),
            path('add-to-cart/<slug>/',add_to_cart,name="add-to-cart")
        ] 

