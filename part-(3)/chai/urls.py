
from django.contrib import admin
from django.urls import path,include
from . import views
#localhost :8000/chai
urlpatterns = [
    path('',views.all_chai,name="all_chai" ),#localhost :8000/chai
    path('order/',views.all_chai_order,name="all_chai_order") , #localhost : 8000/chai/order
    path('<int:chai_id>/',views.chai_detail,name="chai_detail"),  #localhost : 8000/chai/order
    path('chai_store/',views.chai_store_view,name="chai_store") ,
    # path('chai_order',views.chai_working,name="store")
    
]
