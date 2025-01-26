from django import forms 
from .models import ChaiVarity ,Store



class ChaiVarityfrom(forms.Form):
    chai_varity=forms.ModelChoiceField(queryset=ChaiVarity.objects.all()
                                       ,label="Select chai varity") # it work with databse
    
    