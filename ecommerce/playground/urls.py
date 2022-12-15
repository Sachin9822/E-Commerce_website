from django.urls import path
from . import views

app_name = 'ecommerce'
urlpatterns = [
    path('hello/',views.say_hello),
    path('loginn/',views.login_request,name='login'),
    path('signup/',views.signup,name='signup'),  
    path('logout/',views.logout_user,name='logout'),
]
