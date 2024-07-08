from django.shortcuts import render, redirect
from .models import Product, Category, Profile, OneProduct, TwoProduct,ThirdProduct, FourProduct , BsProduct, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from django import forms
from django.db.models import Q
import json
from cart.cart import Cart

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from payment.models import OrderItem
#---------------------------------------------------------Search Section-------------------------------------------------------------------

def search(request):
	# Determine if they filled out the form
	if request.method == "POST":
		searched = request.POST['searched']
		# Query The Products DB Model
		searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
		# Test for null
		if not searched:
			messages.success(request, "That Product Does Not Exist...Please try Again.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})	

#---------------------------------------------------------Profile Section-------------------------------------------------------------------

def update_info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = Profile.objects.get(user__id=request.user.id)
		# Get Current User's Shipping Info
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
		# Get User's Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)		
		if form.is_valid() or shipping_form.is_valid():
			# Save original form
			form.save()
			# Save shipping form
			shipping_form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('home')
		return render(request, "update_info.html", {'form':form, 'shipping_form':shipping_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')



def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

# def update_password_none(request):
# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
	# if request.user:
	# 	current_user = request.user
	# 	# Did they fill out the form
	# 	if request.method  == 'POST':
	# 		form = ChangePasswordForm(current_user, request.POST)
	# 		# Is the form valid
	# 		if form.is_valid():
	# 			form.save()
	# 			messages.success(request, "Your Password Has Been Updated...")
	# 			login(request, current_user)
	# 			return redirect('update_user')
	# 		else:
	# 			for error in list(form.errors.values()):
	# 				messages.error(request, error)
	# 				return redirect('update_password')
	# 	else:
			# form = ChangePasswordForm(current_user)
    # template_name = 'update_password_none.html'
    # email_template_name = 'password_reset_email.html'
    # subject_template_name = 'password_reset_subject.txt'
    # success_message = "We've emailed you instructions for setting your password, " \
    #                   "if an account exists with the email you entered. You should receive them shortly." \
    #                   " If you don't receive an email, " \
    #                   "please make sure you've entered the address you registered with, and check your spam folder."
    # success_url = reverse_lazy('home')

		# return render(request, "update_password_none.html"	)
	# else:
	# 	messages.success(request, "You Must Be Logged In To View That Page...")
	# 	return redirect('home')
	
def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')
	

	
def order(request):
	if request.user.is_authenticated:
		orders = OrderItem.objects.filter(user = request.user).order_by('-id')
		# orders = OrderItem.objects.filter(shipped =False)
		return render(request,"order.html", {'orders':orders})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")	
		return redirect('home')	


def order_summary(request):
	order = Order(request)
	order_products = order
	quantities = order.get_quants
	totals = order.cart_total()
	return render(request, "cart_summary.html", {"cart_products":order_products, "quantities":quantities, "totals":totals})

#---------------------------------------------------------Category Section-------------------------------------------------------------------

def category_summary(request):
	categories = Category.objects.all()
	return render(request, 'category_summary.html', {"categories":categories})	

def category(request, foo):
	# Replace Hyphens with Spaces
	foo = foo.replace('-', ' ')
	# Grab the category from the url
	try:
		# Look Up The Category
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'category.html', {'products':products, 'category':category})
	except:
		messages.success(request, ("That Category Doesn't Exist..."))
		return redirect('home')

#---------------------------------------------------------Book Section-------------------------------------------------------------------

def book(request):
	products = Product.objects.all()
	return render(request, 'book.html', {'products':products})
def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})

#---------------------------------------------------------home Section-------------------------------------------------------------------

def home(request):
	twoproducts = TwoProduct.objects.all()
	return render(request, 'home.html',{"twoproducts":twoproducts})

def oneproduct(request,pk):
	twoproduct = TwoProduct.objects.get(id=pk)
	return render(request, 'twoproduct.html',{'twoproduct':twoproduct})	

# def home(request):
# 	fourproducts = FourProduct.objects.all()
# 	return render(request, 'home.html',{"fourproducts":fourproducts})

#---------------------------------------------------------todaydeal Section-------------------------------------------------------------------

def todaydeal(request):
	twoproducts = TwoProduct.objects.all()
	return render(request, 'todaydeal.html',{'twoproducts':twoproducts})
def twoproduct(request,pk):
	twoproduct = TwoProduct.objects.get(id=pk)
	return render(request, 'twoproduct.html',{'twoproduct':twoproduct})	

#---------------------------------------------------------Best Seller Section-------------------------------------------------------------------

def bestseller(request):
	bsproducts = BsProduct.objects.all()
	return render(request, 'bestseller.html', {'bsproducts':bsproducts})	
def bsproduct(request,pk):
	bsproduct = BsProduct.objects.get(id=pk)
	return render(request, 'bsproduct.html',{'bsproduct':bsproduct})	



# def fourproduct(request,pk):
# 	fourproduct = FourProduct.objects.get(id=pk)
# 	return render(request, 'oneproduct.html',{'fourproduct':fourproduct})	

#---------------------------------------------------------About Section-------------------------------------------------------------------

def about(request):
	return render(request, 'about.html', {})	

#--------------------------------------------------------Cart Section-------------------------------------------------------------------

def cartsummary(request):
	return render(request, 'cart_summary.html', {})	

def cart_summary_bs(request):
	return render(request, 'bs_cartsummary.html', {})	

#---------------------------------------------------------login Section-------------------------------------------------------------------

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			# # Do some shopping cart stuff
			# current_user = Profile.objects.get(user__id=request.user.id)
			# # Get their saved cart from database
			# saved_cart = current_user.old_cart
			# # Convert database string to python dictionary
			# if saved_cart:
			# 	# Convert to dictionary using JSON
			# 	converted_cart = json.loads(saved_cart)
			# 	# Add the loaded cart dictionary to our session
			# 	# Get the cart
			# 	cart = Cart(request)
			# 	# Loop thru the cart and add the items from the database
			# 	for key,value in converted_cart.items():
			# 		cart.db_add(product=key, quantity=value)

			# 	cart = CartOne(request)
			# 	# Loop thru the cart and add the items from the database
			# 	for key,value in converted_cart.items():
			# 		cart.db_add_one(product=key, quantity=value)

			messages.success(request, ("You Have Been Logged In!"))
			return redirect('home')
		else:
			messages.success(request, ("There was an error, please try again..."))
			return redirect('login')

	else:
		return render(request, 'login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You have been logged out...Thanks for shopping by knowledge shop"))
	return redirect('home')

#---------------------------------------------------------Register Section-------------------------------------------------------------------


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
# def register_user(request):
# 	form = SignUpForm()
# 	if request.method == "POST":
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password1']
# 			# log in user
# 			user = authenticate(username=username, password=password)
# 			login(request, user)
# 			messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
# 			return redirect('home')
# 		else:
# 			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
# 			return redirect('register')
# 	else:
# 		return render(request, 'register.html', {'form':form})
	
# def saveform(request):
# 	# form = SignUpForm()
# 	if request.method == "POST":
# 		# if form.is_valid():
# 		# 	form.save()
# 		# 	username = form.cleaned_data['username']
# 		# 	password = form.cleaned_data['password1']
# 		# 	# log in user
# 		# 	user = authenticate(username=username, password=password)
# 		# 	login(request, user)
# 		# 	messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
# 		# 	return redirect('update_info')
# 		# else:
# 		# 	messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
# 		# 	return redirect('register')
# 		# form = SignUpForm(request.POST)
# 		username = request.POST.get('username')
# 		firstname = request.POST.get('firstname')
# 		lastname = request.POST.get('lastname')
# 		email = request.POST.get('email')
# 		password = request.POST.get('password')
# 		# confirm_password = request.POST.get('confirm_password')
# 	en = Registered_user(username=username, firstname=firstname, lastname=lastname, email=email, password=password, )
# 	en.save()
# 	return render(request, 'register.html')
	






