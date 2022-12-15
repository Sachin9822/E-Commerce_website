from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.say_hello),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup')    
]
