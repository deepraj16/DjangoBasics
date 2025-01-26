from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello first word home page")
    return render(request,'index.html')

def about(request):
     #return HttpResponse("hello first word in about page")
    return render(request,'about.html')


def contact(request):
    #return HttpResponse("hello first word in contact page")
    return render(request,'contact.html')