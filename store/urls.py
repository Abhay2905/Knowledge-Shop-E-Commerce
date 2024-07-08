from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from store.views import ResetPasswordView

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.home2, name='home2'),
    path('about/', views.about, name='about'),
    path("book", views.book, name='book'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('product/<int:pk>', views.product, name='product'),
    path('oneproduct/<int:pk>', views.oneproduct, name='oneproduct'),
    path('twoproduct/<int:pk>', views.twoproduct, name='twoproduct'),
    # path('thirdproduct/<int:pk>', views.thirdproduct, name='thirdproduct'),
    # path('fourproduct/<int:pk>', views.fourproduct, name='fourproduct'),
    path('bsproduct/<int:pk>', views.bsproduct, name='bsproduct'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
    path("bestseller/", views.bestseller, name='bestseller'),
    path("todaydeal/", views.todaydeal, name='todaydeal'),
    path("cart_summary/", views.cartsummary, name='cartsummary'),
    path("cart_summary_bs/", views.cart_summary_bs, name='cart_summary_bs'),
    path("order/", views.order, name='order'),
    # path('update_password_none/', views.update_password_none, name='update_password_none'),
    path('update_password_none/', auth_views.PasswordResetView.as_view(template_name='update_password_none.html'), name='update_password_none'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    
]
