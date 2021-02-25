from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,'home.html') # get request from the user and return http request