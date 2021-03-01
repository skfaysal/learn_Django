from django.shortcuts import render
from django.http import HttpResponse
from .models import Diseases

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Faysal'})  # get request from the user and return http request


def add(request):

    if request.method == 'POST':
        num1=request.POST['num1']
        num2=request.POST['num2']
        obj=Diseases()
        for i in range(1000):   
            print(num1,num2)
            obj.num1=num1
            obj.num2=num2
            obj.save()

    context={

    }



    # val1=int(request.GET['num1'])
    # val2=int(request.GET['num2'])

    # res= val1+val2

    return render(request,'home.html',context)

