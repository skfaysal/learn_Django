from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name = 'home') # for getting the home page you have to go home function in views module
]