from django.urls import path
from . import views


urlpatterns = [
    
#-------------------------------------------------------------Book page--------------------------------------------------------------------- 
	path('', views.cart_summary, name="cart_summary"),
	path('add/', views.cart_add, name="cart_add"),
	path('delete/', views.cart_delete, name="cart_delete"),
	path('update/', views.cart_update, name="cart_update"),
#-------------------------------------------------------------Best Seller-------------------------------------------------------------------    
    # path('home/', views.cart_summary_bs, name="cart_summary_bs"),
    path('add_bs/', views.cart_add_bs, name="cart_add_bs"),
    path('delete_bs/', views.cart_delete_bs, name="cart_delete_bs"),
    path('update_bs/', views.cart_update_bs, name="cart_update_bs"),
    
#-------------------------------------------------------------Sale Page-------------------------------------------------------------------------
    path('home/', views.cart_summary_two, name="cart_summary_two"), 
    path('add_two/', views.cart_add_two, name="cart_add_two"),
    path('delete_two/', views.cart_delete_two, name="cart_delete_two"),
    path('update_two/', views.cart_update_two, name="cart_update_two"),
]
