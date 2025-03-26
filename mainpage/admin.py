from django.contrib import admin
from mainpage.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product) 
admin.site.register(Blog)
admin.site.register(ExtendedUser)  
class damAdmin(ImportExportModelAdmin):
    list_display=( 'customer_no','customer_name','customer_username','phone','email','address','Product_id','product_img','Product_quantity','product_price','product_name','status','add_on','total_cost')
    search_fields=('customer_no','customer_username','phone','email','address')
    list_filter=('add_on',)
    ordering=('-add_on',)
admin.site.register(order,damAdmin)
admin.site.register(Returns_Shipping_Policy)
admin.site.register(Privacy_Policy)
admin.site.register(Cancelation_Policy)
admin.site.register(about_compeny)
