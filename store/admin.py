from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile,OneProduct, TwoProduct, ThirdProduct,  FourProduct, BsProduct
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OneProduct)
admin.site.register(TwoProduct)
# admin.site.register(ThirdProduct)
# admin.site.register(FourProduct)
admin.site.register(BsProduct)
admin.site.register(Order)
admin.site.register(Profile)



# Mix profile info and user info
class ProfileInline(admin.StackedInline):
	model = Profile

# class Admin(admin.ModelAdmin):
# 	model = User
# 	field = ["username", "first_name", "last_name", "email"]
# 	inlines = [ProfileInline]

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# # Unregister the old way
# admin.site.unregister(User)

# # Re-Register the new way
# admin.site.register(User, UserAdmin)
