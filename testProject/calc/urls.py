from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name = 'home'), # 1st of all it will show the home.html content
	path('add',views.add,name = 'add') # if add button is pressed it will direct into this path and call add function from views.py
]