from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User

# Register the model on the admin section thing
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

#Create an prder item inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

#Extend our order model
class OrderAdmin(admin.ModelAdmin):
    model = Order    
    readonly_fields = ["date_ordered"]
    # fields = ["user","full_name"]
    inlines = [OrderItemInline]

#Unregidter order model
admin.site.unregister(Order)

#Re-register our order and orderitem
admin.site.register(Order, OrderAdmin)