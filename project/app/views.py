from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    # if request.method=='POST':
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')
    #     city=request.POST.get('city')
        
    #     new_person=Register(Name=name,
    #                         Email=email,
    #                         Password=password,
    #                         City=city)
    #     return HttpResponse(new_person)


    # print(request.method)
    # print(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    city=request.POST.get('city')
    # Register.objects.create(Name=name,
    #                                  Email=email,
    #                                  Password=password,
    #                                  City=city)
    # data=Register.objects.all()
    # print(data)
    data=Register.objects.filter(Email=email)
    print(data)

    if data:
        msg="Email already exist" 
        return render(request,'home.html',{'key':msg})
    else:
        Register.objects.create(Name=name,
                                     Email=email,
                                     Password=password,
                                     City=city)
        msg='registrations '

        return render(request,'register.html',{'key':msg})
    








    