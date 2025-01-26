from django.contrib import admin

# Register your models here.
from .models import ChaiVarity ,ChaiCertifate,ChaiReviews,Store

#normal way to concent woth data of the given
#admin.site.register(ChaiVarity)

# expert way 
class ChaiReviewInline(admin.TabularInline): 
    model=ChaiReviews
    extra=2  # by respect to this colums we are dising the class
    
class ChaiVarietyAdmin(admin.ModelAdmin): 
    list_display=('name','type','date_added')    
    linlines=[ChaiReviewInline]
 
class StoreAdmin(admin.ModelAdmin):
    list_display=('name','locations') 
    filter_horizontal=('chai_varites',)

class ChaiCertifateAdmin(admin.ModelAdmin): 
    list_display=('chai','ceritificate_no')

    

admin.site.register(ChaiVarity,ChaiVarietyAdmin) # you cannt make the 
# admin.site.register(ChaiReviews,ChaiReviewInline) ---> error so you are ingecting admin ti code
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertifate,ChaiCertifateAdmin)

