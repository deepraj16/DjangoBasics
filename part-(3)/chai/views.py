from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.shortcuts import get_object_or_404
import requests

from .forms import ChaiVarityfrom
#working on jina 
#importing databse from backend 
from .models import ChaiVarity
from .models import Store

def all_chai(request):
    chais = ChaiVarity.objects.all()  # from data from backend
    return render(request,'chai/all_chai.html',{'chais' : chais})

def all_chai_order(request): 
    return render(request,'chai/all_order.html')

def chai_detail(request,chai_id):
    chai =get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai})

def chai_store_view(request):
    stores=None
    if request.method=='POST':
        form=ChaiVarityfrom(request.POST)
        if form.is_valid():
            chai_varity=form.cleaned_data['chai_varity']
            stores=Store.objects.filter(chai_varites=chai_varity)
    else:
        form=ChaiVarityfrom()        

    return render(request,'chai/chai_stores.html',{'store':stores , 'form':form})


# how to working data transfer from front-end to backend 
# i have use java scrpit working 
# what about the ai and ml how to you focus on it or working with you have start 
# and working start 
# def chai_working(request): 
#     #return HttpRequest("hellow word")    
#     chai_store=Store.objects.all()
#     return render(request,'chai/all_order.html')
