from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import User 


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]
    name=models.CharField(max_length=100)
    image =models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    descrption=models.TextField(default='')
    price=models.IntegerField(default=12)
    def __str__(self):
        return self.name
    

 # relection the code for given 
 # many to many 
 # one to many 
 # many to one 

 # one to many 

class ChaiReviews(models.Model):
    # requred filed which can yes to connet to auther tables
    chai=models.ForeignKey(ChaiVarity,on_delete=models.CASCADE , related_name="review")
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # the colums of this colums 
    rating =models.IntegerField()
    comment =models.TextField() 
    data_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} reviews for {self.chai.name}'    
    
    
#many to many 

class Store(models.Model): 
    name=models.CharField(max_length=100)
    locations=models.CharField(max_length=100)
    chai_varites=models.ManyToManyField(ChaiVarity,related_name="stores")

    def __str__(self):
        return self.name 


 # one to one 


class ChaiCertifate(models.Model):
    chai =models.OneToOneField(ChaiVarity, on_delete=models.CASCADE ,related_name='Certicates')
    ceritificate_no=models.CharField(max_length=50)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_util=models.DateTimeField()

    def __str__(self):
        return f"chai cetificaion for {self.name.chai}"
    
    
# migrate the chanage

    
    

