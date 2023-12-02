from django.contrib import admin
from . models import Payment,OrderProduct,Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name' , 'phone', 'order_total', 'is_ordered','created_at' , 'status']
    list_filter = ['status','is_ordered']
    search_fields = ['order_number','first_name','last_number']
    list_per_page = 15
    
admin.site.register(Order,OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)